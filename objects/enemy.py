import pygame
from objects.actor import Actor
pygame.init()

class Enemy(Actor):
    def __init__(self,x,y,w,h,color,img,spd=[0,0],maxHP,name="enemy"):
        super().__init__(x,y,w,h,color,img,spd,maxHP,name)

    def act(self):
        pass #have enemy call attack under certain circumstances

    def attack(self):
        pass
