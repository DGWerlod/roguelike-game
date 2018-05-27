import pygame, constants
pygame.init()

player = pygame.transform.scale(pygame.image.load("img/chrissyc.png"),(constants.playerW,constants.playerH))
simplePlayer = pygame.image.load("img/simplePlayer.png")
