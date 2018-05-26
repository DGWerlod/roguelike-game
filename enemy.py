import pygame, actor
pygame.init()

class Enemy(actor.Actor):
    def __init__(self,x,y,w,h,color,img,spd=[0,0],maxHP,name="enemy"):
        super().__init__(x,y,w,h,color,img,spd,maxHP,name)

    def act(self):
        pass #have enemy call attack under certain circumstances

    def attack(self):
        pass
