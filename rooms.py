import constants
from objects.item import Item
from objects.obstruction import Obstruction
from objects.enemy import Enemy
from objects.boss import Boss
from objects.spawner import Spawner

stdObstructions = [
    Obstruction(0, 0, constants.roomL + 10, constants.gameH), # left
    Obstruction(constants.roomR - 10, 0, constants.roomL + 10, constants.gameH), # right
    Obstruction(0, 0, constants.gameW, 10), # top
    Obstruction(0, constants.roomB - 10, constants.gameW, constants.roomT + 10) # bottom
]

class Room(object):
    def __init__(self, roomType, enemies, items, obstructions=stdObstructions):
        self.type = roomType
        self.enemies = enemies
        self.items = items
        self.obstructions = obstructions
        self.doors = []

# START
start = Room("standard",[],[],[])

# STANDARD
standard = [
    Room("standard", [Enemy("apple")], []),
    Room("standard", [Enemy("apple"), Enemy("cherry")],[Item(1)]),
    Room("standard", [Enemy("cherry"), Enemy("cherry")], [Item(1,25),Item(0,-25)]),
    Room("standard", [Spawner("banana")], [])
]

# SHOP
shop = [
    Room("shop", [], [Item(3)]),
    Room("shop", [], [Item(4)])
]

# DISH
dish = [
    Room("dish", [], [Item(0,-5,-10)])
]

# RISK
risk = [
    Room("risk", [Boss("peep")], []),
    Room("risk", [], [Item(8)])
]

# BOSS
boss = [
    Room("boss", [Boss("peep")], [Item(7)])
]
