import pygame
from objects.rect import Rect
pygame.init()

class Obstruction(Rect):
    def __init__(self,x,y,w,h,color,spd,name="obstruction"):
        super().__init__(x,y,w,h,color,spd,name)