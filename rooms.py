import constants
from objects.item import Item
from objects.obstruction import Obstruction
from objects.enemy import Enemy
from objects.boss import Boss
from objects.spawner import Spawner

stdObstructions = [Obstruction(0,0,110,constants.gameH),
Obstruction(790,0,110,constants.gameH),
Obstruction(0,0,constants.gameW,10),
Obstruction(0,490,constants.gameW,110)]

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
    Room("standard", [Enemy("apple"), Enemy("cherry")],[Item(1,20)]),
    Room("standard", [Enemy("cherry"), Enemy("cherry")], [Item(1,20,25),Item(0,20,-25)]),
    Room("standard", [Spawner("banana")], [])
]

# SHOP
shop = [
    Room("shop", [], [Item(3,20)]),
    Room("shop", [], [Item(4,20)])
]

# DISH
dish = [
    Room("dish", [], [Item(0,20,-5,-10)])
]

# RISK
risk = [
    Room("risk", [Boss("peep")], []),
    Room("risk", [], [Item(8,50)])
]

# BOSS
boss = [
    Room("boss", [Boss("peep")], [Item(7,60)])
]
