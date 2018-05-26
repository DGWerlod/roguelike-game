import pygame, rect
pygame.init()

class Obstruction(rect.Rect):
    def __init__(self,x,y,w,h,color,spd,name="obstruction"):
        super().__init__(x,y,w,h,color,spd,name)
