import pygame
from img import images
from objects.rect import Rect
pygame.init()

class Door(Rect):
    def __init__(self,x,y,w,h,type="rect",name="rect"):
        super().__init__(x,y,w,h,None,None,[0,0],name)
        self.type = type
    def draw(self, ctx, state):
        ctx.blit(images.getDoor(self.type,self.name,state),(self.x,self.y))
    def go(self, ctx, state):
        self.pos()
        self.draw(ctx, state)
