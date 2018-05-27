import pygame, math, random, constants
from controls import keyboard, mouse
from objects.player import Player
from img import images
from rooms import rooms
pygame.init()

ctx = pygame.display.set_mode((constants.gameW,constants.gameH))
pygame.display.set_caption("CircleGame")
clock = pygame.time.Clock()

curFloor = []
curRoom = rooms[0]

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

def startFloor():
    nextFloor = []
    numRooms = 4 + 8 + math.floor(math.random()*4)
    for i in range(numRooms):
        nextFloor.append(rooms[math.floor(math.random())])

def main():
    while True:
        listen()

        # Reset BG
        ctx.blit(images.bg,(0,0))

        # Update All Entities
        for d in curRoom["doors"]:
            d.go(ctx)
        for i in curRoom["items"]:
            i.go(ctx)
        for e in curRoom["enemies"]:
            e.go(ctx, curRoom)
        player.go(ctx, curRoom)

        # Update Window
        pygame.display.update()
        clock.tick(60)

main()
