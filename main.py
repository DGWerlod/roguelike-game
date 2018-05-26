import pygame, math, random, constants
from objects.player import Player
pygame.init()

ctx = pygame.display.set_mode((constants.gameW,constants.gameH))
pygame.display.set_caption("CircleGame")
clock = pygame.time.Clock()

playerImg = pygame.image.load("img/chrissyc.png")
player = Player(0,0,30,60,(0,0,0),playerImg,[5,5],50)

def close():
    pygame.quit()
    quit()

def listen():
    for event in pygame.event.get():
        info = pygame.mouse.get_pressed()
        if info[0] == 1 and mouse['held'] == 0:
            mouse['click'] = 1
            mouse['held'] = 1
        elif info[0] == 1 and mouse['held'] == 1:
            mouse['click'] = 0
        elif info[0] == 0:
            mouse['click'] = 0
            mouse['held'] = 0
        mouse['pos'] = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            elif event.type == pygame.KEYDOWN:
                for p in presets:
                    if event.key == presets[p]:
                        controls[p] = True
            elif event.type == pygame.KEYUP:
                for p in presets:
                    if event.key == presets[p]:
                        controls[p] = False

def main():
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()

        player.go(ctx)

        pygame.display.update()
        clock.tick(60)

main()
