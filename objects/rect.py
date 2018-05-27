import pygame
from objects.entity import Entity
pygame.init()

class Rect(Entity):
    def __init__(self,x,y,w,h,color,spd,name="rect"):
        super().__init__(x,y,color,spd,name)
        self.w = w
        self.h = h
    def draw(self, ctx):
        pygame.draw.rect(ctx,self.color,(self.x,self.y,self.w,self.h))
