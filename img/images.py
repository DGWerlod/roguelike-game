import pygame, constants
pygame.init()

peach = pygame.image.load("img/peach.png")
halfPeach = pygame.image.load("img/halfpeach.png")
foodStamp = pygame.image.load("img/foodstamp.png")
player1 = pygame.transform.scale(pygame.image.load("img/chefspud_default.png"),(60,120))
player2 = pygame.transform.scale(pygame.image.load("img/chefspud_reverse.png"),(60,120))

apple = pygame.transform.scale(pygame.image.load("img/badappple.png"),(60,60))
cherry = pygame.transform.scale(pygame.image.load("img/cherryvil.png"),(60,60))
banana = pygame.transform.scale(pygame.image.load("img/banana.png"),(60,60))
peep = pygame.transform.scale(pygame.image.load("img/peepboss.png"),(120,120))
bunny = pygame.transform.scale(pygame.image.load("img/evilbunny.png"),(60,60))

marshmallow = pygame.image.load("img/marshmallow.png")
frenchFry = pygame.image.load("img/frenchfry.png")

# chrissyC = pygame.image.load("img/chrissyc.png")
# simplePlayer = pygame.image.load("img/simplePlayer.png")

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
},
"dish": {
    "w": [
        pygame.image.load("img/doors/dish/dish_W_closed.png"),
        pygame.image.load("img/doors/dish/dish_W_open.png")
    ],
    "a": [
        pygame.image.load("img/doors/dish/dish_A_closed.png"),
        pygame.image.load("img/doors/dish/dish_A_open.png")
    ],
    "s": [
        pygame.image.load("img/doors/dish/dish_S_closed.png"),
        pygame.image.load("img/doors/dish/dish_S_open.png")
    ],
    "d": [
        pygame.image.load("img/doors/dish/dish_D_closed.png"),
        pygame.image.load("img/doors/dish/dish_D_open.png")
    ]
},
"shop": {
    "w": [
        pygame.image.load("img/doors/shop/shop_W_closed.png"),
        pygame.image.load("img/doors/shop/shop_W_open.png")
    ],
    "a": [
        pygame.image.load("img/doors/shop/shop_A_closed.png"),
        pygame.image.load("img/doors/shop/shop_A_open.png")
    ],
    "s": [
        pygame.image.load("img/doors/shop/shop_S_closed.png"),
        pygame.image.load("img/doors/shop/shop_S_open.png")
    ],
    "d": [
        pygame.image.load("img/doors/shop/shop_D_closed.png"),
        pygame.image.load("img/doors/shop/shop_D_open.png")
    ]
}
}

backgrounds = {
    "standard": pygame.image.load("img/background.png"),
    "risk": pygame.image.load("img/salt_background.png"),
    "boss": pygame.image.load("img/cuttingboard_background.png"),
    "dish": pygame.image.load("img/dish_background.png"),
    "shop": pygame.image.load("img/cookbook_background.png")
}

if id == 0: # peach
    target.maxHP += 2
elif id == 1: # knife
    target.dmg += 1
elif id == 2: # basil
    pass
elif id == 3: # paprika
    target.atkSpd -= 2
elif id == 4: # pepper
    target.spd += 1
elif id == 5: # salt
    pass
elif id == 6: # tumeric
    pass

items = [
    pygame.transform.scale(pygame.image.load("img/peach.png"),(30,30)),
    pygame.transform.scale(pygame.image.load("img/foodstamp.png"),(30,30)),
    pygame.image.load("img/spices/basil.png"),
    pygame.image.load("img/spices/paprika.png"),
    pygame.image.load("img/spices/pepper.png"),
    pygame.image.load("img/spices/salt.png"),
    pygame.image.load("img/spices/turmeric.png"),
    pygame.transform.scale(pygame.image.load("img/peach.png"),(60,60)),
    pygame.transform.scale(pygame.image.load("img/knife.png"),(30,30))
]

def getImage(name):
    if name == "apple":
        return apple
    if name == "peep":
        return peep
    if name == "bunny":
        return bunny
    if name == "peach":
        return half
    if name == "halfpeach":
        return halfPeach
    if name == "cherry":
        return cherry
    if name == "banana":
        return banana

def getDoor(type, name, state): # 0 = closed, 1 = open
    return doors[type][name][state]
