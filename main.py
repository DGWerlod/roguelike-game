import pygame, math, random, constants, generator
from controls import keyboard, mouse
from objects.rect import Rect
from objects.hud import HUD
from objects.minimap import Minimap
from objects.enemy import Enemy
from objects.player import Player
from objects.spawner import Spawner
from objects.boss import Boss
from img import images
from logic import collisions

from pygame.locals import *
flags = DOUBLEBUF

pygame.init()

ctx = pygame.display.set_mode((constants.gameW,constants.gameH), flags)
ctx.set_alpha(None)
pygame.display.set_caption("Roguelike")
clock = pygame.time.Clock()

muli = pygame.font.Font("fonts/muli.ttf",15)
muliBig = pygame.font.Font("fonts/muli.ttf",30)
muliBiggest = pygame.font.Font("fonts/muli.ttf",70)

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

def trySpawn(enemy, room, map):
    spawn = None
    if enemy.name == "peep":
        if random.randint(0,math.ceil(1000/map.level)) == 0:
            spawn = Enemy("bunny")
            if random.randint(0,math.ceil(100/map.level)) == 0: # i.e. 1 in 100,000 chance per frame
                spawn = Boss("peep")
    elif isinstance(enemy, Spawner):
        if enemy.spawnCD == 0:
            spawn = Spawner(enemy.name,math.ceil(enemy.spawnSpd*(map.level+1)/map.level))
    if spawn != None:
        spawn.setup()
        spawn.x, spawn.y = (constants.gameW-spawn.w)/2, (constants.gameH-spawn.h)/2
        spawn.x += random.randint(0,300)-150
        spawn.y += random.randint(0,300)-150
        room["enemies"].append(spawn)

def nextFloor(map):
    curFloor = generator.newFloor()
    level = 1
    if not map == None:
        level = map.level+1
    map = Minimap(curFloor,level)
    for y in range(constants.gridLength):
        for x in range(constants.gridLength):
            if not curFloor[y][x] == None:
                curRoom = curFloor[y][x]
                curPos = [y,x]
    return curFloor, curRoom, curPos, map

def main():

    state = 0
    enemiesCleared = False
    bullets = []
    running = True
    projectile = None

    player = Player()
    hud = HUD(player)

    while running:
        running = listen(running)

        if state == 0:
            ctx.blit(images.splash,(0,0))
            beginText = muliBig.render("Press Enter",True,constants.lightpurple)
            beginTextRECT = beginText.get_rect()
            beginTextRECT.right = constants.gameW - 20
            beginTextRECT.bottom = constants.gameH - 15
            ctx.blit(beginText,beginTextRECT)

            if keyboard.controls["keyEnter"]:
                state = 1
                curFloor, curRoom, curPos, map = nextFloor(None)

        elif state == 1:
            # Reset BG
            ctx.blit(images.backgrounds[curRoom["type"]],(0,0))

            if enemiesCleared:
                for c in curRoom["doors"]:
                    key = c.name
                    if collisions.rectangles(player,constants.clearZones[key]):
                        transitionFlag = False
                        if key == "w" and keyboard.controls["keyW"]:
                            curPos[0] -= 1
                            player.y = constants.gameH - 110 - constants.playerH - 20
                            transitionFlag = True
                        elif key == "a" and keyboard.controls["keyA"]:
                            curPos[1] -= 1
                            player.x = constants.gameW - 110 - constants.playerW - 20
                            transitionFlag = True
                        elif key == "s" and keyboard.controls["keyS"]:
                            curPos[0] += 1
                            player.y = 10 + 20
                            transitionFlag = True
                        elif key == "d" and keyboard.controls["keyD"]:
                            curPos[1] += 1
                            player.x = 110 + 20
                            transitionFlag = True
                        if transitionFlag:
                            curRoom = curFloor[curPos[0]][curPos[1]]
                            bullets = []
                            enemiesCleared = False
                if curRoom["type"] == "boss":
                    x = (constants.gameW-80)/2
                    y = (constants.gameH-80)/2
                    ctx.blit(images.teleporter,(x,y))
                    if pygame.Rect(x,y,80,80).contains(pygame.Rect(player.x,player.y + player.h/2,player.w,player.h/2)):
                        # print(" ") # divides this floor map and the previous floor map
                        curFloor, curRoom, curPos, map = nextFloor(map)
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
                elif isinstance(e,Boss) or isinstance(e,Spawner):
                    trySpawn(e,curRoom,map)

            projectile = player.go(ctx, curRoom)
            projectile = getProjectile(projectile, bullets)

            if player.hp <= 0:
                state = 2
                gameOverText = muliBiggest.render("Game Over",True,constants.black)
                gameOverTextRECT = gameOverText.get_rect()
                gameOverTextRECT.center = (constants.gameW/2,constants.gameH/2 - 30)
                ctx.blit(gameOverText,gameOverTextRECT)
                retryText = muliBig.render("Press Enter to Restart",True,constants.black)
                retryTextRECT = retryText.get_rect()
                retryTextRECT.center = (constants.gameW/2,constants.gameH/2 + 30)
                ctx.blit(retryText,retryTextRECT)

            # Debug
            fps = muli.render(str(round(clock.get_fps(),1)),True,constants.black)
            ctx.blit(fps,(840,575))

        elif state == 2:

            if keyboard.controls["keyEnter"]:
                state = 1
                enemiesCleared = False
                bullets = []
                player.__init__()
                hud.__init__(player)
                curFloor, curRoom, curPos, map = nextFloor(None)

            continue

        # Update Window
        pygame.display.update()
        clock.tick(30)
    pygame.quit()

main()
