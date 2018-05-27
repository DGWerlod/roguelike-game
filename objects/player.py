import pygame, math
from objects.actor import Actor
from controls import keyboard
import constants
pygame.init()

class Player(Actor):
    def __init__(self,x,y,w,h,color,img,maxHP,spd,name="player"):
        super().__init__(x,y,w,h,color,img,maxHP,spd,name)
        self.items = []
        self.phase = 0

    def pos(self, room):
        if keyboard.controls['keyW'] == True:
            self.y -= self.spd[1]
            if not super().canMove(room) or self.y < 0:
                self.y += self.spd[1]
        if keyboard.controls['keyA'] == True:
            self.x -= self.spd[0]
            if not super().canMove(room) or self.x < 0:
                self.x += self.spd[0]
        if keyboard.controls['keyS'] == True:
            self.y += self.spd[1]
            if not super().canMove(room) or self.y + self.h > constants.gameH:
                self.y -= self.spd[1]
        if keyboard.controls['keyD'] == True:
            self.x += self.spd[0]
            if not super().canMove(room) or self.x + self.w > constants.gameW:
                self.x -= self.spd[0]

    def act(self):
        pass

    def animate(self):
        self.phase += 1
        if self.phase == 60:
            self.phase = 0

    def draw(self, ctx):
        self.animate()
        ctx.blit(self.img[math.floor(self.phase/30)], (self.x,self.y))
