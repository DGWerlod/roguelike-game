import pygame, math, random, constants
from player import Player
pygame.init()

ctx = pygame.display.set_mode((constants.gameW,constants.gameH))
pygame.display.set_caption("CircleGame")
clock = pygame.time.Clock()

playerImg = pygame.image.load("img/chrissyc.png")
player = Player(0,0,30,60,(0,0,0),playerImg,[5,5],50)

def close():
    pygame.quit()
    quit()

def main():
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()

        player.go(ctx)

        pygame.display.update()
        clock.tick(60)

main()
