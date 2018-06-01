import pygame, math
from img import images
from objects.rect import Rect
from objects.bullet import Bullet
import constants

class Actor(Rect):
    def __init__(self,x,y,w,h,color,img,maxHP,spd=[0,0],name="actor"):
        super().__init__(x,y,w,h,color,img,spd,name)
        self.maxHP = maxHP
        self.hp = maxHP

    def attack(self, target):
        selfCenterX = self.x + self.w/2
        selfCenterY = self.y + self.h/2
        theta = math.atan2((target.y + target.h/2 - selfCenterY), (target.x + target.w/2 - selfCenterX))
        return Bullet(selfCenterX-5,selfCenterY-5,10,10,images.marshmallow,theta,self.dmg,"bad")

    def pos(self, room):
        if self.canMove(room):
            self.x += self.spd[0]
            self.y += self.spd[1]

    def go(self, ctx, room):
        self.pos(room)
        self.draw(ctx)
