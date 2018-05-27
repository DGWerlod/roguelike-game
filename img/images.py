import pygame, constants
pygame.init()

bg = pygame.image.load("img/background.png")

doorTop = [pygame.image.load("img/doors/door_W_closed.png"), pygame.image.load("img/doors/door_W_open.png")]
doorLeft = [pygame.image.load("img/doors/door_A_closed.png"), pygame.image.load("img/doors/door_A_open.png")]
doorRight = [pygame.image.load("img/doors/door_D_closed.png"), pygame.image.load("img/doors/door_D_open.png")]
doorBottom = [pygame.image.load("img/doors/door_S_closed.png"), pygame.image.load("img/doors/door_S_open.png")]

player1 = pygame.transform.scale(pygame.image.load("img/chefspud_default.png"),(60,120))
player2 = pygame.transform.scale(pygame.image.load("img/chefspud_reverse.png"),(60,120))
enemy = pygame.transform.scale(pygame.image.load("img/badappple.png"),(60,60))
chrissyC = pygame.image.load("img/chrissyc.png")
simplePlayer = pygame.image.load("img/simplePlayer.png")

lemon = pygame.image.load("img/lemonafraid.png")
