import pygame, math, random, constants
from objects.item import Item
from objects.obstruction import Obstruction
from objects.character import Character
from objects.enemy import Enemy
from objects.player import Player
from controls import keyboard, mouse
from img import images
pygame.init()

ctx = pygame.display.set_mode((constants.gameW,constants.gameH))
pygame.display.set_caption("CircleGame")
clock = pygame.time.Clock()

curRoom = {
"obstructions":
[
    Obstruction(800,500,100,100)
],
"enemies":
[
    Enemy(700,0,30,30,constants.black,images.chrissyC,20)
],
"items":
[
    Item(0,300,300,20,20,constants.black)
]
}

player = Player(0,0,constants.playerW,constants.playerH,constants.black,images.player,50,[5,5])

def close():
    pygame.quit()
    quit()

def listen():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            else:
                keyboard.listen(event)
                mouse.listen()

def main():
    while True:
        ctx.fill(constants.black)
        listen()
        player.go(ctx, curRoom)
        pygame.display.update()
        clock.tick(60)

main()
