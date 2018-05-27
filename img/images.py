import pygame, constants
pygame.init()

bg = pygame.image.load("img/background.png")

player1 = pygame.transform.scale(pygame.image.load("img/chefspud_default.png"),(60,120))
player2 = pygame.transform.scale(pygame.image.load("img/chefspud_reverse.png"),(60,120))
apple = pygame.transform.scale(pygame.image.load("img/badappple.png"),(60,60))
peep = pygame.image.load("img/peepboss.png")
bunny = pygame.image.load("img/evilbunny.png")
chrissyC = pygame.image.load("img/chrissyc.png")
simplePlayer = pygame.image.load("img/simplePlayer.png")

lemon = pygame.image.load("img/lemonafraid.png")

doors = {
"standard": {
    "w": [
        pygame.image.load("img/doors/standard/door_W_closed.png"),
        pygame.image.load("img/doors/standard/door_W_open.png")
    ],
    "a": [
        pygame.image.load("img/doors/standard/door_A_closed.png"),
        pygame.image.load("img/doors/standard/door_A_open.png")
    ],
    "s": [
        pygame.image.load("img/doors/standard/door_S_closed.png"),
        pygame.image.load("img/doors/standard/door_S_open.png")
    ],
    "d": [
        pygame.image.load("img/doors/standard/door_D_closed.png"),
        pygame.image.load("img/doors/standard/door_D_open.png")
    ]
},
"risk": {
    "w": [
        pygame.image.load("img/doors/salt_pepper/salt_W_closed.png"),
        pygame.image.load("img/doors/salt_pepper/salt_W_open.png")
    ],
    "a": [
        pygame.image.load("img/doors/salt_pepper/salt_A_closed.png"),
        pygame.image.load("img/doors/salt_pepper/salt_A_open.png")
    ],
    "s": [
        pygame.image.load("img/doors/salt_pepper/salt_S_closed.png"),
        pygame.image.load("img/doors/salt_pepper/salt_S_open.png")
    ],
    "d": [
        pygame.image.load("img/doors/salt_pepper/salt_D_closed.png"),
        pygame.image.load("img/doors/salt_pepper/salt_D_open.png")
    ]
},
"boss": {
    "w": [
        pygame.image.load("img/doors/knife/knife_W_closed.png"),
        pygame.image.load("img/doors/knife/knife_W_open.png")
    ],
    "a": [
        pygame.image.load("img/doors/knife/knife_A_closed.png"),
        pygame.image.load("img/doors/knife/knife_A_open.png")
    ],
    "s": [
        pygame.image.load("img/doors/knife/knife_S_closed.png"),
        pygame.image.load("img/doors/knife/knife_S_open.png")
    ],
    "d": [
        pygame.image.load("img/doors/knife/knife_D_closed.png"),
        pygame.image.load("img/doors/knife/knife_D_open.png")
    ]
# },
# "dish": {
#     "w": [
#         pygame.image.load("img/doors/dish/dish_W_closed.png"),
#         pygame.image.load("img/doors/dish/dish_W_open.png")
#     ],
#     "a": [
#         pygame.image.load("img/doors/dish/dish_A_closed.png"),
#         pygame.image.load("img/doors/dish/dish_A_open.png")
#     ],
#     "s": [
#         pygame.image.load("img/doors/dish/dish_S_closed.png"),
#         pygame.image.load("img/doors/dish/dish_S_open.png")
#     ],
#     "d": [
#         pygame.image.load("img/doors/dish/dish_D_closed.png"),
#         pygame.image.load("img/doors/dish/dish_D_open.png")
#     ]
# },
# "shop": {
#     "w": [
#         pygame.image.load("img/doors/shop/shop_W_closed.png"),
#         pygame.image.load("img/doors/shop/shop_W_open.png")
#     ],
#     "a": [
#         pygame.image.load("img/doors/shop/shop_A_closed.png"),
#         pygame.image.load("img/doors/shop/shop_A_open.png")
#     ],
#     "s": [
#         pygame.image.load("img/doors/shop/shop_S_closed.png"),
#         pygame.image.load("img/doors/shop/shop_S_open.png")
#     ],
#     "d": [
#         pygame.image.load("img/doors/shop/shop_D_closed.png"),
#         pygame.image.load("img/doors/shop/shop_D_open.png")
#     ]
}
}

backgrounds = {
"standard": pygame.image.load("img/background.png"),
"risk": pygame.image.load("img/salt_background.png"),
"boss": pygame.image.load("img/cuttingboard_background.png"),
# "dish": pygame.image.load(""),
"shop": pygame.image.load("img/cookbook_background.png")
}

def getImage(name):
    if name == "apple":
        return apple
    if name == "peep":
        return peep
    if name == "bunny":
        return bunny

def getDoor(type, name, state): # 0 = closed, 1 = open
    return doors[type][name][state]
