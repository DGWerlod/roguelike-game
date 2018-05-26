import pygame
from objects.rect import Rect
pygame.init()

class Item(Rect):
    def __init__(self,id,x,y,w,h,color,spd,name="item"):
        super().__init__(x,y,w,h,color,spd,name)
            self.id = id
            self.removeFlag = False
    def activate(self, target): pass
