import pygame, math, random, constants
from controls import keyboard, mouse
from objects.player import Player
from img import images
from rooms import rooms
pygame.init()

ctx = pygame.display.set_mode((constants.gameW,constants.gameH))
pygame.display.set_caption("CircleGame")
clock = pygame.time.Clock()

curRoom = rooms[0]

player = Player(0,0,constants.playerW,constants.playerH,constants.black,images.player,50,[5,5])

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

def main():
    while True:
        listen()

        # Reset BG
        ctx.fill(constants.black)

        # Update All Entities
        for o in curRoom["obstructions"]:
            o.go(ctx)
        for i in curRoom["items"]:
            i.go(ctx)
        for e in curRoom["enemies"]:
            e.go(ctx, curRoom)
        player.go(ctx, curRoom)

        # Update Window
        pygame.display.update()
        clock.tick(60)

main()
