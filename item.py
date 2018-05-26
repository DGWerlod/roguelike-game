import pygame, rect
pygame.init()

class Item(rect.Rect):
    def __init__(self,id,x,y,w,h,color,spd,name="item"):
        super().__init__(x,y,w,h,color,spd,name)
            self.id = id
            self.removeFlag = False
    def activate(self, target): pass
