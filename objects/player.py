import pygame, math
from objects.bullet import Bullet
from objects.actor import Actor
from img import images
from controls import keyboard, mouse
import constants
pygame.init()

class Player(Actor):
    def __init__(self,x,y,w,h,color,img,maxHP,spd,atkSpd,name="player"):
        super().__init__(x,y,w,h,color,img,maxHP,spd,name)
        self.dmg = 1
        self.items = []
        self.phase = 0
        self.atkSpd = atkSpd
        self.attackCD = 0

    def pos(self, room):
        if keyboard.controls['keyW'] == True:
            self.y -= self.spd[1]
            if not super().canMove(room):
                self.y += self.spd[1]
        if keyboard.controls['keyA'] == True:
            self.x -= self.spd[0]
            if not super().canMove(room):
                self.x += self.spd[0]
        if keyboard.controls['keyS'] == True:
            self.y += self.spd[1]
            if not super().canMove(room):
                self.y -= self.spd[1]
        if keyboard.controls['keyD'] == True:
            self.x += self.spd[0]
            if not super().canMove(room):
                self.x -= self.spd[0]

    def animate(self):
        self.phase += 1
        if self.phase == 60:
            self.phase = 0

    def attack(self):
        selfCenterX = self.x + self.w/2
        selfCenterY = self.y + self.h/2
        theta = math.atan2(mouse.mouse['pos'][1]-selfCenterY, mouse.mouse['pos'][0]-selfCenterX)
        return Bullet(selfCenterX-5,selfCenterY-5,10,10,images.frenchFry,theta,self.dmg,"good")

    def draw(self, ctx):
        self.animate()
        ctx.blit(self.img[math.floor(self.phase/30)], (self.x,self.y))

    def go(self, ctx, room):
        super().go(ctx, room)
        if self.attackCD > 0:
            self.attackCD -= 1
        elif mouse.mouse['click'] == True:
            self.attackCD = self.atkSpd
            return self.attack()
        return None
