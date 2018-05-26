import pygame
from objects.actor import Actor
pygame.init()

class Player(Actor):
    def __init__(self,x,y,w,h,color,img,spd,maxHP,name="player"):
        super().__init__(x,y,w,h,color,img,spd,maxHP,name)
        self.items = []

    def pos(self):
        pass #have some keyboard response here

    def act(self):
        pass
