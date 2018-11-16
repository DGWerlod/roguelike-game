import pygame
from objects.rect import Rect
pygame.font.init()

# GENERAL VARIABLES
gameW, gameH = 900, 600
roomL, roomT, roomR, roomB = 100, 100, gameW-100, gameH-100
playerW, playerH = 60, 120
gridLength = 5

# COLORS
black = (0,0,0)
grey = (128,128,128)
miniGrey = (178, 178, 178)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
yellow = (255,255,0)
lightPurple = (86, 95, 120)

# FONTS
source, sizes = "fonts/muli.ttf", [15, 20, 30, 70]
muli = {}
for s in sizes:
    muli[str(s)] = pygame.font.Font(source, s)

# WASD
W, A, S, D = 0, 1, 2, 3

# STATES
AUTHORS, START = 0, 1
GAME = 2
PAUSE, GAMEOVER = 3, 4

# PAUSELOCK STATES
pauseNone = 0
pauseEnter = 1
pauseExit = 2

# DOOR
doorSlim, doorWide = 100, 150
LRDoor = (gameH - doorWide) / 2
TBDoor = (gameW - doorWide) / 2

# CLEAR ZONES
clearZones = {
    "w": Rect(gameW/2 - doorWide/2 + doorWide/3, 10, doorWide/3, 5, grey),
    "a": Rect(roomL + 10, gameH/2 - doorWide/2 + doorWide/3, 5, doorWide/3, grey),
    "s": Rect(gameW/2 - doorWide/2 + doorWide/3, roomB - 15, doorWide/3, 5, grey),
    "d": Rect(roomR - 15, gameH/2 - doorWide/2 + doorWide/3, 5, doorWide/3, grey)
}