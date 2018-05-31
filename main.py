import pygame, math, random, constants, generator
from controls import keyboard, mouse
from objects.rect import Rect
from objects.enemy import Enemy
from objects.player import Player
from img import images
from logic import collisions

from pygame.locals import *
flags = DOUBLEBUF

pygame.init()

ctx = pygame.display.set_mode((constants.gameW,constants.gameH), flags)
ctx.set_alpha(None)
pygame.display.set_caption("Roguelike")
clock = pygame.time.Clock()

curFloor = []
curRoom = {}
curPos = []

muli = pygame.font.Font("fonts/muli.ttf",15)
player = Player(170,240,10,[5,5],15)

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

def trySpawn(enemy, room):
    if random.randint(0,450) == 0:
        bunnySpawn = Enemy("bunny")
        bunnySpawn.setup()
        bunnySpawn.x, bunnySpawn.y = (constants.gameW-bunnySpawn.w)/2, (constants.gameH-bunnySpawn.h)/2
        bunnySpawn.x += random.randint(0,300)-150
        bunnySpawn.y += random.randint(0,300)-150
        room["enemies"].append(bunnySpawn)

def renderStamps():
    stamps = muli.render(str(player.stamps),True,constants.black)
    stampsRECT = stamps.get_rect()
    stampsRECT.right = 85 + 20
    stampsRECT.top = 35
    return stamps, stampsRECT

def nextFloor(curFloor, curRoom, curPos):
    curFloor = generator.newFloor()
    for y in range(constants.gridLength):
        for x in range(constants.gridLength):
            if not curFloor[y][x] == None:
                curRoom = curFloor[y][x]
                curPos = [y,x]
    return curFloor, curRoom, curPos

def main(curFloor, curRoom, curPos):

    enemiesCleared = False
    bullets = []
    running = True
    projectile = None
    stamps, stampsRECT = renderStamps()
    stampsLastFrame = player.stamps

    while running:
        running = listen(running)

        # Reset BG
        ctx.blit(images.backgrounds[curRoom["type"]],(0,0))

        if enemiesCleared:
            for c in curRoom["doors"]:
                key = c.name
                if collisions.rectangles(player,constants.clearZones[key]):
                    if key == "w":
                        curPos[0] -= 1
                        player.y = constants.gameH - 110 - constants.playerH - 20
                    elif key == "a":
                        curPos[1] -= 1
                        player.x = constants.gameW - 110 - constants.playerW - 20
                    elif key == "s":
                        curPos[0] += 1
                        player.y = 10 + 20
                    elif key == "d":
                        curPos[1] += 1
                        player.x = 110 + 20
                    curRoom = curFloor[curPos[0]][curPos[1]]
                    bullets = []
                    enemiesCleared = False
            if curRoom["type"] == "boss":
                x = (constants.gameW-80)/2
                y = (constants.gameH-80)/2
                ctx.blit(images.teleporter,(x,y))
                if pygame.Rect(x,y,80,80).contains(pygame.Rect(player.x,player.y + player.h/2,player.w,player.h/2)):
                    curFloor, curRoom, curPos = nextFloor(curFloor, curRoom, curPos)
        else:
            enemiesCleared = enemyCheck(curRoom)

        # Update All Entities
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
            elif e.name == "peep":
                trySpawn(e,curRoom)


        projectile = player.go(ctx, curRoom)
        projectile = getProjectile(projectile, bullets)

        location = 50
        for i in range(math.floor(player.hp/2)):
            ctx.blit(images.peach,(location,15))
            location += 20
        if player.hp % 2 == 1 and player.hp > 0:
            ctx.blit(images.halfPeach,(location,15))

        ctx.blit(images.foodStamp,(85,35))

        if player.stamps != stampsLastFrame:
            stamps, stampsRECT = renderStamps()
        ctx.blit(stamps,stampsRECT)
        stampsLastFrame = player.stamps

        # Debug
        fps = muli.render(str(round(clock.get_fps(),1)),True,constants.black)
        ctx.blit(fps,(840,575))

        # Update Window
        pygame.display.update()
        clock.tick(30)
    pygame.quit()

curFloor, curRoom, curPos = nextFloor(curFloor, curRoom, curPos)
main(curFloor, curRoom, curPos)
