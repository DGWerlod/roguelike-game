import pygame
from objects.enemy import Enemy

class Boss(Enemy):
    def __init__(self,name="boss",spd=[0,0]):
        super().__init__(name,spd)
