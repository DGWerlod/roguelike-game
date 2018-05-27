import pygame, math, random, constants, generator
from controls import keyboard, mouse
from objects.rect import Rect
from objects.player import Player
from img import images
from rooms import rooms
from logic import collisions
pygame.init()

ctx = pygame.display.set_mode((constants.gameW,constants.gameH))
pygame.display.set_caption("Roguelike")
clock = pygame.time.Clock()

curFloor = []
curRoom = {}
curPos = []

player = Player(170,240,constants.playerW,constants.playerH,
                    constants.black,[images.player1,images.player2],50,[4,4])

def close():
    pygame.quit()
    quit()

def listen():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            else:
                keyboard.listen(event)
                mouse.listen()

def enemyCheck(room):
    allEnemiesDead = 1
    for e in room["enemies"]:
        if e.hp > 0:
            allEnemiesDead = 0
            break
    return allEnemiesDead

def main(curFloor, curRoom, curPos):
    delayTimer = 0
    enemiesCleared = 0
    while True:
        if delayTimer > 0:
            delayTimer -= 1
        if delayTimer == 0:
            enemiesCleared = 1
        listen()

        # Reset BG
        ctx.blit(images.backgrounds[curRoom["type"]],(0,0))    

        # Update All Entities
        for d in curRoom["doors"]:
            d.go(ctx, enemiesCleared)
        for i in curRoom["items"]:
            i.go(ctx)
        for e in curRoom["enemies"]:
            e.go(ctx, curRoom)
        player.go(ctx, curRoom)

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
                    delayTimer = 600
                    enemiesCleared = 0
        else:pass
            # enemiesCleared = enemyCheck(curRoom)

        # Update Window
        pygame.display.update()
        clock.tick(60)

curFloor = generator.newFloor()
for y in range(constants.gridLength):
    for x in range(constants.gridLength):
        if not curFloor[y][x] == None:
            curRoom = curFloor[y][x]
            curPos = [y,x]
main(curFloor, curRoom, curPos)
