import pygame, entity
pygame.init()

class Rect(entity.Entity):
    def __init__(self,x,y,w,h,color,spd,name="rect"):
        super().__init__(x,y,color,spd,name)
        self.w = w
        self.h = h
    def draw(self):
        pygame.draw.rect(ctx,color,(x,y,w,h))
