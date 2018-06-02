import pygame, constants

peach = pygame.image.load("img/items/peach.png")
halfPeach = pygame.image.load("img/items/halfpeach.png")
foodStamp = pygame.image.load("img/items/foodstamp.png")
player1 = pygame.transform.scale(pygame.image.load("img/characters/chefspud_default.png"),(60,120))
player2 = pygame.transform.scale(pygame.image.load("img/characters/chefspud_reverse.png"),(60,120))
marshmallow = pygame.image.load("img/bullets/marshmallow.png")
frenchFry = pygame.image.load("img/bullets/frenchfry.png")

# chrissyC = pygame.image.load("img/chrissyc.png")
# simplePlayer = pygame.image.load("img/simplePlayer.png")
# lemon = pygame.image.load("img/characters/lemonafraid.png")

teleporter = pygame.transform.scale(pygame.image.load("img/teleporter.png"),(80,80))
splash = pygame.image.load("img/splash.png")

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
    "standard": pygame.image.load("img/bg/background.png"),
    "risk": pygame.image.load("img/bg/salt_background.png"),
    "boss": pygame.image.load("img/bg/cuttingboard_background.png"),
    "dish": pygame.image.load("img/bg/dish_background.png"),
    "shop": pygame.image.load("img/bg/cookbook_background.png")
}

items = [
    pygame.transform.scale(pygame.image.load("img/items/peach.png"),(30,30)),
    pygame.transform.scale(pygame.image.load("img/items/foodstamp.png"),(30,30)),
    pygame.image.load("img/items/spices/basil.png"),
    pygame.image.load("img/items/spices/paprika.png"),
    pygame.image.load("img/items/spices/pepper.png"),
    pygame.image.load("img/items/spices/salt.png"),
    pygame.image.load("img/items/spices/turmeric.png"),
    pygame.transform.scale(pygame.image.load("img/items/peach.png"),(60,60)),
    pygame.transform.scale(pygame.image.load("img/items/knife.png"),(30,30))
]

icons = [
    None,
    None,
    pygame.transform.scale(pygame.image.load("img/items/spices/basil.png"),(15,15)),
    pygame.transform.scale(pygame.image.load("img/items/spices/paprika.png"),(15,15)),
    pygame.transform.scale(pygame.image.load("img/items/spices/pepper.png"),(15,15)),
    pygame.transform.scale(pygame.image.load("img/items/spices/salt.png"),(15,15)),
    pygame.transform.scale(pygame.image.load("img/items/spices/turmeric.png"),(15,15)),
    None,
    pygame.transform.scale(pygame.image.load("img/items/knife.png"),(15,15))
]

enemies = {
    "apple": pygame.transform.scale(pygame.image.load("img/characters/badappple.png"),(60,60)),
    "cherry": pygame.transform.scale(pygame.image.load("img/characters/cherryvil.png"),(60,60)),
    "banana": pygame.transform.scale(pygame.image.load("img/characters/banana.png"),(60,60)),
    "peep": pygame.transform.scale(pygame.image.load("img/characters/peepboss.png"),(120,120)),
    "bunny": pygame.transform.scale(pygame.image.load("img/characters/evilbunny.png"),(60,60))
}
