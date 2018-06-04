import pygame, math, random, constants, generator
from img import images
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

def gameOver(ctx):
    gameOverText = constants.muli["70"].render("Game Over",True,constants.black)
    gameOverTextRECT = gameOverText.get_rect()
    gameOverTextRECT.center = (constants.gameW/2,constants.gameH/2 - 30)
    ctx.blit(gameOverText,gameOverTextRECT)
    retryText = constants.muli["30"].render("Press Enter to Restart",True,constants.black)
    retryTextRECT = retryText.get_rect()
    retryTextRECT.center = (constants.gameW/2,constants.gameH/2 + 30)
    ctx.blit(retryText,retryTextRECT)

def main():

    state = 0
    enemiesCleared = False
    bullets = []
    running = True
    projectile = None

    player = Player()
    hud = HUD(player)
    teleporter = Teleporter()

    while running:
        running = listen(running)

        if state == 0:
            ctx.blit(images.splash,(0,0))
            beginText = constants.muli["30"].render("Press Enter",True,constants.lightpurple)
            beginTextRECT = beginText.get_rect()
            beginTextRECT.right = constants.gameW - 20
            beginTextRECT.bottom = constants.gameH - 15
            ctx.blit(beginText,beginTextRECT)

            if keyboard.controls["keyEnter"]:
                state = 1
                curFloor, curRoom, curPos, map = generator.nextFloor(None)

        elif state == 1:
            # Reset BG
            ctx.blit(images.backgrounds[curRoom["type"]],(0,0))

            if enemiesCleared:
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
                state = 2
                gameOver(ctx)

            # Debug
            fps = constants.muli["15"].render(str(round(clock.get_fps(),1)),True,constants.black)
            ctx.blit(fps,(840,575))

        elif state == 2:

            if keyboard.controls["keyEnter"]:
                state = 1
                enemiesCleared = False
                bullets = []
                player.__init__()
                hud.__init__(player)
                curFloor, curRoom, curPos, map = generator.nextFloor(None)

            continue

        # Update Window
        pygame.display.update()
        clock.tick(30)
    pygame.quit()

main()
