import pygame, constants
pygame.init()

player1 = pygame.transform.scale(pygame.image.load("img/chefspud_default.png"),(60,120))
player2 = pygame.transform.scale(pygame.image.load("img/chefspud_reverse.png"),(60,120))
enemy = pygame.transform.scale(pygame.image.load("img/badappple.png"),(60,60))
chrissyC = pygame.image.load("img/chrissyc.png")
simplePlayer = pygame.image.load("img/simplePlayer.png")
