import pygame
from objects.rect import Rect
import constants
from logic import collisions

pygame.init()

class Actor(Rect):
    def __init__(self,x,y,w,h,color,img,maxHP,spd=[0,0],name="actor"):
        super().__init__(x,y,w,h,color,img,spd,name)
        self.maxHP = maxHP
        self.hp = maxHP

    def act(self): pass

    def canMove(self, room):
        for o in room["obstructions"]:
            if collisions.rectangles(self,o):
                return False
        return True

    def pos(self, room):
        if self.canMove(room):
            self.x += self.spd[0]
            self.y += self.spd[1]

    def draw(self, ctx):
        ctx.blit(self.img, (self.x,self.y))

    def go(self, ctx, room):
        self.pos(room)
        self.draw(ctx)
