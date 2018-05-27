import pygame
from objects.actor import Actor
from controls import keyboard
import constants
pygame.init()

class Player(Actor):
    def __init__(self,x,y,w,h,color,img,maxHP,spd,name="player"):
        super().__init__(x,y,w,h,color,img,maxHP,spd,name)
        self.items = []

    def pos(self):
        if keyboard.controls['keyW'] == True:
            self.y -= self.spd[1]
            if not self.canMove() or self.y < 0:
                self.y += self.spd[1]
        if keyboard.controls['keyA'] == True:
            self.x -= self.spd[0]
            if not self.canMove() or self.x < 0:
                self.x += self.spd[0]
        if keyboard.controls['keyS'] == True:
            self.y += self.spd[1]
            if not self.canMove() or self.y + self.h > constants.gameH:
                self.y -= self.spd[1]
        if keyboard.controls['keyD'] == True:
            self.x += self.spd[0]
            if not self.canMove() or self.x + self.w > constants.gameW:
                self.x -= self.spd[0]

    def act(self):
        pass

    def go(self, ctx):
        self.pos()
        self.draw(ctx)
