from objects.rect import Rect

# GENERAL VARIABLES
gameW, gameH = 900, 600
playerW, playerH = 60, 120
gridLength = 5

# COLORS
black = (0,0,0)
grey = (128,128,128)

# WASD
W, A, S, D = 0, 1, 2, 3

# DOOR
doorSlim, doorWide = 100, 150

# CLEAR ZONES
clearZones = {
    "w": Rect(gameW/2 - doorWide/2,10,doorWide,5,grey),
    "a": Rect(110,gameH/2 - doorWide/2,5,doorWide,grey),
    "s": Rect(gameW/2 - doorWide/2,485,doorWide,5,grey),
    "d": Rect(785,gameH/2 - doorWide/2,5,doorWide,grey)
}

# ENEMY DATA   HP,FIRE RATE IN TICKS (1/60),DMG
enemyData = {
    "apple": [60,60,3,60,1],
    "cherry": [60,60,1,20,1],
    "banana": [60,60,4,40,1],
    "peep": [120,120,15,60,2],
    "bunny": [60,60,1,60,1]
}
