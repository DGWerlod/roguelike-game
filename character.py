import pygame, actor
pygame.init()

class Character(actor.Actor):
    def __init__(self,x,y,w,h,color,img,spd=[0,0],maxHP,name="character"):
        super().__init__(x,y,w,h,color,img,spd,maxHP,name)
