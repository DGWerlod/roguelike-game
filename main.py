import pygame, math, random, constants, generator
from img import images
from sound import sounds
from logic import collisions
from controls import keyboard, mouse
from objects.hud import HUD
from objects.teleporter import Teleporter
from objects.player import Player

from pygame.locals import *
flags = DOUBLEBUF

pygame.init()

ctx = pygame.display.set_mode((constants.gameW,constants.gameH), flags)
ctx.set_alpha(None)
pygame.display.set_caption("Roguelike")
clock = pygame.time.Clock()

def listen(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == sounds.END_FLAG:
            pygame.mixer.music.pause()
            pygame.mixer.music.rewind()
            pygame.mixer.music.play()
            pygame.mixer.music.set_pos(sounds.overtureLoopTime)
        else:
            keyboard.listen(event)
            mouse.listen()
    return running

def enemyCheck(room):
    allEnemiesDead = True
    for e in room["enemies"]:
        if e.hp > 0:
            allEnemiesDead = False
            break
    return allEnemiesDead

def getProjectile(projectile,bullets):
    if projectile != None:
        bullets.append(projectile)
    return None

def pause(ctx):
    pygame.draw.rect(ctx,constants.grey,(200,200,constants.gameW-400,constants.gameH-400))
    ctx.blit(constants.pauseText,constants.pauseTextRECT)
    ctx.blit(constants.resumeText,constants.resumeTextRECT)

def gameOver(ctx):
    ctx.blit(constants.gameOverText,constants.gameOverTextRECT)
    ctx.blit(constants.retryText,constants.retryTextRECT)

def main():

    pygame.mixer.music.play()
    pygame.mixer.music.set_pos(70.0)

    state = constants.START
    enemiesCleared = False
    bullets = []
    running = True
    projectile = None

    player = Player()
    hud = HUD(player)
    teleporter = Teleporter()

    pauseLock = constants.pauseNone

    while running:
        running = listen(running)

        if state == constants.START:
            ctx.blit(images.splash,(0,0))
            ctx.blit(constants.beginText,constants.beginTextRECT)

            if keyboard.controls["keyEnter"]:
                state = constants.GAME
                curFloor, curRoom, curPos, map = generator.nextFloor(None)

        elif state == constants.GAME:
            # Check pause

            if keyboard.controls["keyEscape"]:
                if pauseLock == constants.pauseNone:
                    state = constants.PAUSE
                    pauseLock = constants.pauseEnter
            else:
                pauseLock = constants.pauseNone

            # Reset BG
            ctx.blit(images.backgrounds[curRoom["type"]],(0,0))

            if enemiesCleared:
                # Test for room changes
                for c in curRoom["doors"]:
                    key = c.name
                    if collisions.rectangles(player,constants.clearZones[key]):
                        if key == "w" and keyboard.controls["keyW"]:
                            curPos[0] -= 1
                            player.y = constants.gameH - 110 - constants.playerH - 20
                        elif key == "a" and keyboard.controls["keyA"]:
                            curPos[1] -= 1
                            player.x = constants.gameW - 110 - constants.playerW - 20
                        elif key == "s" and keyboard.controls["keyS"]:
                            curPos[0] += 1
                            player.y = 10 + 20
                        elif key == "d" and keyboard.controls["keyD"]:
                            curPos[1] += 1
                            player.x = 110 + 20
                        if curRoom != curFloor[curPos[0]][curPos[1]]:
                            curRoom = curFloor[curPos[0]][curPos[1]]
                            bullets = []
                            enemiesCleared = False
                if curRoom["type"] == "boss":
                    if teleporter.go(ctx, player):
                        curFloor, curRoom, curPos, map = generator.nextFloor(map)
            else:
                enemiesCleared = enemyCheck(curRoom)

            # Update All Entities
            hud.go(ctx, player)
            map.go(ctx, curPos)

            for d in curRoom["doors"]:
                d.go(ctx, enemiesCleared)
            for i in curRoom["items"]:
                if not i.consumedFlag:
                    i.go(ctx, player, enemiesCleared)
            for b in bullets:
                b.go(ctx, curRoom, player)
                if b.removeFlag:
                    bullets.remove(b)
            for e in curRoom["enemies"]:
                projectile = e.go(ctx, curRoom, player)
                projectile = getProjectile(projectile, bullets)
                if e.hp <= 0:
                    curRoom["enemies"].remove(e)
                generator.trySpawn(e,curRoom,map)

            projectile = player.go(ctx, curRoom)
            projectile = getProjectile(projectile, bullets)

            if player.hp <= 0:
                state = constants.GAMEOVER
                gameOver(ctx)

            # Debug
            fps = constants.muli["15"].render(str(round(clock.get_fps(),1)),True,constants.black)
            ctx.blit(fps,(840,575))

        elif state == constants.PAUSE:
            pause(ctx)
            if keyboard.controls["keyEscape"]:
                if pauseLock == constants.pauseNone:
                    state = constants.GAME
                    pauseLock = constants.pauseExit
            else:
                pauseLock = constants.pauseNone

        elif state == constants.GAMEOVER:

            if keyboard.controls["keyEnter"]:
                state = constants.GAME
                enemiesCleared = False
                bullets = []
                player.__init__()
                hud.__init__(player)
                curFloor, curRoom, curPos, map = generator.nextFloor(None)

            continue # Skips updating window

        # Update Window
        pygame.display.update()
        clock.tick(30)

    pygame.quit()

main()
