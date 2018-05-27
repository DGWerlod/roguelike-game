import pygame, math, random, constants
from objects.player import Player
from controls import keyboard, mouse
from img import images
pygame.init()

ctx = pygame.display.set_mode((constants.gameW,constants.gameH))
pygame.display.set_caption("CircleGame")
clock = pygame.time.Clock()

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

        ctx.fill(constants.black)

        listen()

        player.go(ctx)

        pygame.display.update()
        clock.tick(60)

main()
