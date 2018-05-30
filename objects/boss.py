import pygame
from object.enemy import Enemy
pygame.init()

class Boss(Enemy):
    def __init__(self,x,y,w,h,color,maxHP,atkSpd,dmg,name="boss",spd=[0,0]):
        super().__init__(x,y,w,h,color,maxHP,atkSpd,dmg,name,spd)

pygame.quit()
