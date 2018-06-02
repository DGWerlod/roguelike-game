import pygame
from objects.rect import Rect
pygame.font.init()

# GENERAL VARIABLES
gameW, gameH = 900, 600
playerW, playerH = 60, 120
gridLength = 5

# COLORS
black = (0,0,0)
grey = (128,128,128)
minigrey = (178,178,178)
yellow = (255,255,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

# FONTS
muli = pygame.font.Font("fonts/muli.ttf",15)

# WASD
W, A, S, D = 0, 1, 2, 3

# DOOR
doorSlim, doorWide = 100, 150
LRDoor = (gameH - doorWide) / 2
TBDoor = (gameW - doorWide) / 2

# CLEAR ZONES
clearZones = {
    "w": Rect(gameW/2 - doorWide/2,10,doorWide,5,grey),
    "a": Rect(110,gameH/2 - doorWide/2,5,doorWide,grey),
    "s": Rect(gameW/2 - doorWide/2,485,doorWide,5,grey),
    "d": Rect(785,gameH/2 - doorWide/2,5,doorWide,grey)
}

# ENEMY DATA   HP,FIRE RATE IN TICKS (1/60),DMG
enemyData = {
    "apple": [60,60,3,40,1],
    "cherry": [60,60,1,20,1],
    "banana": [60,60,5,60,1],
    "peep": [120,120,15,60,2],
    "bunny": [60,60,1,60,1]
}
