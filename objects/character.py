import pygame
from objects.actor import Actor
pygame.init()

class Character(Actor):
    def __init__(self,x,y,w,h,color,img,spd=[0,0],maxHP,name="character"):
        super().__init__(x,y,w,h,color,img,spd,maxHP,name)