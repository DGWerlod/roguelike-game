import constants
from img import images
from objects.rect import Rect
from objects.item import Item
from objects.obstruction import Obstruction
from objects.character import Character
from objects.enemy import Enemy

rooms = [
# Room 1
{
"obstructions":
[
    Obstruction(0,0,110,constants.gameH,constants.grey),
    Obstruction(790,0,110,constants.gameH,constants.grey),
    Obstruction(0,0,constants.gameW,10,constants.grey),
    Obstruction(0,490,constants.gameW,110,constants.grey)
],
"enemies":
[
    Enemy(650,270,60,60,constants.black,images.enemy,20)
],
"items":
[
    Item(0,300,300,20,20,constants.black)
],
"doors":
[
    Rect((constants.gameW-150)/2,0,150,100,constants.grey,images.saltTop[1])
]
},

# Room 2
]
