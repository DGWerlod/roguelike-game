import pygame
from objects.actor import Actor
from img import images
pygame.init()

class Enemy(Actor):
    def __init__(self,x,y,w,h,color,maxHP,name="enemy",spd=[0,0]):
        super().__init__(x,y,w,h,color,None,maxHP,spd,name)

    def act(self):
        pass #have enemy call attack under certain circumstances

    def attack(self):
        pass

    def draw(self, ctx):
        ctx.blit(images.getImage(self.name),(self.x,self.y))
