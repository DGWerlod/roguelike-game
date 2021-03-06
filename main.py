import pygame, constants, generator
from img import images
from sound import sounds
from fonts import text
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
            sounds.changeMusic(sounds.overtureLoopTime)
        else:
            keyboard.listen(event)
            mouse.listen()
    return running

def enemyCheck(room):
    allEnemiesDead = True
    for e in room.enemies:
        if e.hp > 0:
            allEnemiesDead = False
            break
    return allEnemiesDead

def enterRoom(curRoom):
    enemiesCleared = enemyCheck(curRoom)
    if not enemiesCleared:
        if curRoom.type != "boss":
            sounds.play("slam1")
        else:
            sounds.play("slam2")
    return enemiesCleared

def main():

    pygame.mixer.music.play()

    state = constants.AUTHORS
    enemiesCleared = False
    bullets = []
    running = True

    player = Player()
    hud = HUD(player)
    teleporter = Teleporter()

    curFloor, curRoom, curPos, minimap = None, None, None, None

    while running:
        running = listen(running)

        if state == constants.AUTHORS:
            for t in text.authorsList:
                ctx.blit(t[0],t[1])

            if keyboard.controls["keyEnter"]:
                sounds.changeMusic(sounds.overtureGoTime)
            if keyboard.controls["keyEnter"] or pygame.mixer.music.get_pos() > sounds.overtureGoTime*1000:
                state = constants.START
                keyboard.enterLock = True

        if state == constants.START:
            ctx.blit(images.splash,(0,0))
            ctx.blit(text.begin,text.beginRECT)
            if keyboard.controls["keyEnter"]:
                if not keyboard.enterLock:
                    state = constants.GAME
                    curFloor, curRoom, curPos, minimap = generator.nextFloor(None)
            elif keyboard.enterLock:
                keyboard.enterLock = False

        elif state == constants.GAME:

            # Check pause
            if keyboard.controls["keyEscape"]:
                if keyboard.pauseLock == constants.pauseNone:
                    state = constants.PAUSE
                    keyboard.pauseLock = constants.pauseEnter
            else:
                keyboard.pauseLock = constants.pauseNone

            # Reset BG
            ctx.blit(images.backgrounds[curRoom.type],(0,0))

            if enemiesCleared:
                # Test for room changes
                for c in curRoom.doors:
                    key = c.name
                    if collisions.rectangles(player,constants.clearZones[key]):

                        spaceBuffer = 20
                        if key == "w" and keyboard.controls["keyW"]:
                            curPos[0] -= 1
                            player.y = constants.roomB - 10 - constants.playerH - spaceBuffer
                        elif key == "a" and keyboard.controls["keyA"]:
                            curPos[1] -= 1
                            player.x = constants.roomR - 10 - constants.playerW - spaceBuffer
                        elif key == "s" and keyboard.controls["keyS"]:
                            curPos[0] += 1
                            player.y = 10 + spaceBuffer
                        elif key == "d" and keyboard.controls["keyD"]:
                            curPos[1] += 1
                            player.x = constants.roomL + 10 + spaceBuffer
                        if curRoom != curFloor[curPos[0]][curPos[1]]:
                            curRoom = curFloor[curPos[0]][curPos[1]]
                            bullets = []
                            enemiesCleared = enterRoom(curRoom)

                if curRoom.type == "boss":
                    if teleporter.go(ctx, player):
                        curFloor, curRoom, curPos, minimap = generator.nextFloor(minimap)
                        enemiesCleared = enterRoom(curRoom)
            else:
                # Test for door unlock
                enemiesCleared = enemyCheck(curRoom)
                if enemiesCleared:
                    sounds.play("unlock")

            # Update All Entities
            hud.go(ctx, player)
            minimap.go(ctx, curPos)

            for d in curRoom.doors:
                d.go(ctx, enemiesCleared)
            for i in curRoom.items:
                if not i.consumedFlag:
                    i.go(ctx, player, enemiesCleared)
            for b in bullets:
                b.go(ctx, curRoom, player)
                if b.removeFlag:
                    bullets.remove(b)
            for e in curRoom.enemies:
                projectile = e.go(ctx, curRoom, player)
                if projectile is not None:
                    bullets.append(projectile)
                if e.hp <= 0:
                    curRoom.enemies.remove(e)
                generator.trySpawn(e, curRoom, minimap)

            projectile = player.go(ctx, curRoom)
            if projectile is not None:
                bullets.append(projectile)

            if player.hp <= 0:
                state = constants.GAMEOVER
                ctx.blit(text.gameOver, text.gameOverRECT)
                ctx.blit(text.retry, text.retryRECT)

            # Debug
            fps = constants.muli["15"].render(str(round(clock.get_fps(),1)),True,constants.black)
            ctx.blit(fps,(840,575))

        elif state == constants.PAUSE:
            # pause(ctx)

            ctx.blit(images.backgrounds[curRoom.type], (0, 0))
            hud.go(ctx, player)
            minimap.go(ctx, curPos)
            ctx.blit(images.playerPause, (constants.roomL + 50, constants.roomR + 50))
            ctx.blit(text.spud, text.spudRECT)
            ctx.blit(text.pause, text.pauseRECT)

            if keyboard.controls["keyEscape"]:
                if keyboard.pauseLock == constants.pauseNone:
                    state = constants.GAME
                    keyboard.pauseLock = constants.pauseExit
            else:
                keyboard.pauseLock = constants.pauseNone

        elif state == constants.GAMEOVER:

            if keyboard.controls["keyEnter"]:
                state = constants.GAME
                enemiesCleared = False
                bullets = []
                player.__init__()
                hud.__init__(player)
                curFloor, curRoom, curPos, minimap = generator.nextFloor(None)

            continue # Skips updating window

        # Update Window
        pygame.display.update()
        clock.tick(30)

    pygame.quit()

main()
