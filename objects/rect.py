import pygame
from objects.entity import Entity
pygame.init()

class Rect(Entity):
    def __init__(self,x,y,w,h,color,img=None,spd=[0,0],name="rect"):
        super().__init__(x,y,color,spd,name)
        self.w = w
        self.h = h
        self.img = img
    def draw(self, ctx):
        if self.img != None:
            ctx.blit(self.img,(self.x,self.y))
        else:
            pygame.draw.rect(ctx,self.color,(self.x,self.y,self.w,self.h))
