import constants
from img import images
from objects.item import Item
from objects.obstruction import Obstruction
from objects.character import Character
from objects.enemy import Enemy

rooms = [
# Room 1
{
"obstructions":
[
    Obstruction(800,500,100,100,constants.grey)
],
"enemies":
[
    Enemy(700,0,60,60,constants.black,images.enemy,20)
],
"items":
[
    Item(0,300,300,20,20,constants.black)
]
},

# Room 2
]
