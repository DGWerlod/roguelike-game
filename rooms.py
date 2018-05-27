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
"type": "standard",
"obstructions":
[
    Obstruction(0,0,110,constants.gameH,constants.grey),
    Obstruction(790,0,110,constants.gameH,constants.grey),
    Obstruction(0,0,constants.gameW,10,constants.grey),
    Obstruction(0,490,constants.gameW,110,constants.grey)
],
"enemies":
[
    Enemy(650,270,60,60,constants.black,20,60,1,"apple")
],
"items":
[
    Item(0,300,300,20,20,constants.black)
],
"doors": []
},

# Room 2
{
"type": "boss",
"obstructions":
[
    Obstruction(0,0,110,constants.gameH,constants.grey),
    Obstruction(790,0,110,constants.gameH,constants.grey),
    Obstruction(0,0,constants.gameW,10,constants.grey),
    Obstruction(0,490,constants.gameW,110,constants.grey)
],
"enemies":
[
    Enemy((constants.gameW-60)/2,(constants.gameH-60)/2,120,120,constants.black,100,60,1,"peep"),
    Enemy((constants.gameW-60)/2,(constants.gameH-60)/2-40,60,60,constants.black,20,60,1,"bunny"),
    Enemy((constants.gameW-60)/2,(constants.gameH-60)/2+40,60,60,constants.black,20,60,1,"bunny"),
    Enemy((constants.gameW-60)/2-40,(constants.gameH-60)/2,60,60,constants.black,20,60,1,"bunny"),
    Enemy((constants.gameW-60)/2+40,(constants.gameH-60)/2,60,60,constants.black,20,60,1,"bunny")
],
"items":
[
    Item(5,(constants.gameW-60)/2,(constants.gameH-60)/2,60,60,constants.black) #Knife
],
"doors": []
},
]
