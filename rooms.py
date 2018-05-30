import constants, random
from img import images
from objects.rect import Rect
from objects.item import Item
from objects.obstruction import Obstruction
from objects.character import Character
from objects.enemy import Enemy

stdObstructions = [Obstruction(0,0,110,constants.gameH),
Obstruction(790,0,110,constants.gameH),
Obstruction(0,0,constants.gameW,10),
Obstruction(0,490,constants.gameW,110)]

# STANDARD

standard = [
{
"type": "standard",
"obstructions": stdObstructions,
"enemies": [Enemy("apple")],
"items": [],
"doors": []
},

{
"type": "standard",
"obstructions": stdObstructions,
"enemies": [Enemy("apple"), Enemy("cherry")],
"items": [Item(1,20)],
"doors": []
},

{
"type": "standard",
"obstructions": stdObstructions,
"enemies": [Enemy("cherry"), Enemy("cherry")],
"items": [Item(1,20,25),Item(0,20,-25)],
"doors": []
},

{
"type": "standard",
"obstructions": stdObstructions,
"enemies": [Enemy("banana")],
"items":[],
"doors": []
}
]

# SHOP

shop = [
{
"type": "shop",
"obstructions": stdObstructions,
"enemies": [],
"items": [Item(3,20)],
"doors": []
},

{
"type": "shop",
"obstructions": stdObstructions,
"enemies": [],
"items": [Item(4,20)],
"doors": []
}
]

# DISH

dish = [
{
"type": "dish",
"obstructions": stdObstructions,
"enemies": [],
"items": [Item(0,20,-5,-10)],
"doors": []
}
]

# RISK

risk = [
{
"type": "risk",
"obstructions": stdObstructions,
"enemies": [Enemy("peep")],
"items": [],
"doors": []
},

{
"type": "risk",
"obstructions": stdObstructions,
"enemies": [],
"items": [Item(8,50)],
"doors": []
}
]

# BOSS

boss = [
{
"type": "boss",
"obstructions": stdObstructions,
"enemies": [Enemy("peep")],
"items": [Item(7,60)],
"doors": []
}
]
