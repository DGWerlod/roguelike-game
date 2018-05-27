import pygame, constants
pygame.init()

bg = pygame.image.load("img/background.png")

doorTop = [pygame.image.load("img/doors/standard/door_W_closed.png"), pygame.image.load("img/doors/standard/door_W_open.png")]
doorLeft = [pygame.image.load("img/doors/standard/door_A_closed.png"), pygame.image.load("img/doors/standard/door_A_open.png")]
doorRight = [pygame.image.load("img/doors/standard/door_D_closed.png"), pygame.image.load("img/doors/standard/door_D_open.png")]
doorBottom = [pygame.image.load("img/doors/standard/door_S_closed.png"), pygame.image.load("img/doors/standard/door_S_open.png")]
saltTop = [pygame.image.load("img/doors/salt_pepper/salt_W_closed.png"), pygame.image.load("img/doors/salt_pepper/salt_W_open.png")]
saltLeft = [pygame.image.load("img/doors/salt_pepper/salt_A_closed.png"), pygame.image.load("img/doors/salt_pepper/salt_A_open.png")]
saltRight = [pygame.image.load("img/doors/salt_pepper/salt_D_closed.png"), pygame.image.load("img/doors/salt_pepper/salt_D_open.png")]
saltBottom = [pygame.image.load("img/doors/salt_pepper/salt_S_closed.png"), pygame.image.load("img/doors/salt_pepper/salt_S_open.png")]

player1 = pygame.transform.scale(pygame.image.load("img/chefspud_default.png"),(60,120))
player2 = pygame.transform.scale(pygame.image.load("img/chefspud_reverse.png"),(60,120))
apple = pygame.transform.scale(pygame.image.load("img/badappple.png"),(60,60))
peep = pygame.image.load("img/peepboss.png")
chrissyC = pygame.image.load("img/chrissyc.png")
simplePlayer = pygame.image.load("img/simplePlayer.png")

lemon = pygame.image.load("img/lemonafraid.png")

def getImage(name):
    if name == "apple":
        return apple
