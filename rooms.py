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

# normal, shop, dishwasher, risk, boss
# Item(0,300,300,20,20)

standard = [
{
"type": "standard",
"obstructions": stdObstructions,
"enemies":
[
    Enemy("apple")
],
"items":[

],
"doors": []
},

{
"type": "standard",
"obstructions": stdObstructions,
"enemies":
[
    Enemy("apple"),
    Enemy("cherry")
],
"items":
[
    Item(1,(constants.gameW-20)/2,(constants.gameH-20)/2,20,20)
],
"doors": []
},

# Room 2
{
"type": "standard",
"obstructions": stdObstructions,
"enemies":
[
    Enemy("cherry"),
    Enemy("cherry")
],
"items":
[
    Item(1,(constants.gameW-20)/2+25,(constants.gameH-20)/2,20,20),
    Item(0,(constants.gameW-20)/2-25,(constants.gameH-20)/2,20,20)
],
"doors": []
},

# Room 3
{
"type": "standard",
"obstructions": stdObstructions,
"enemies":
[
    Enemy("banana")
],
"items":
[

],
"doors": []
}
]

shop = [
{
"type": "shop",
"obstructions": stdObstructions,
"enemies": [],
"items":
[
    Item(3,(constants.gameW-20)/2,(constants.gameH-20)/2,20,20)
],
"doors": []
},
{
"type": "shop",
"obstructions": stdObstructions,
"enemies": [],
"items":
[
    Item(4,(constants.gameW-20)/2,(constants.gameH-20)/2,20,20)
],
"doors": []
}
]

dish = [
{
"type": "dish",
"obstructions": stdObstructions,
"enemies": [],
"items":
[
    Item(0,(constants.gameW-20)/2-5,(constants.gameH-20)/2-10,20,20)
],
"doors": []
}
]

risk = [
{
"type": "risk",
"obstructions": stdObstructions,
"enemies":
[
    Enemy("peep")
],
"items": [],
"doors": []
},
{
"type": "risk",
"obstructions": stdObstructions,
"enemies": [],
"items":
[
    Item(8,(constants.gameW-50)/2,(constants.gameH-50)/2,50,50)
],
"doors": []
}
]

boss = [
{
"type": "boss",
"obstructions": stdObstructions,
"enemies":
[
    Enemy("peep")
],
"items":
[
    Item(7,(constants.gameW-60)/2,(constants.gameH-60)/2,60,60)
],
"doors": []
}

]
