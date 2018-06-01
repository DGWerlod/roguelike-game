import pygame, constants
from objects.actor import Actor
from objects.bullet import Bullet
from img import images

class Enemy(Actor):
    def __init__(self,name="enemy",spd=[0,0]):
        data = constants.enemyData
        super().__init__(0,0,data[name][0],data[name][1],None,None,data[name][2],spd,name)
        self.atkSpd = data[name][3]
        self.attackCD = data[name][3]
        self.dmg = data[name][4]

    def setup(self):
        self.img = images.enemies[self.name]

    def go(self, ctx, room, target):
        super().go(ctx,room)
        if self.attackCD > 0:
            self.attackCD -= 1
            return None
        else:
            self.attackCD = self.atkSpd
            return self.attack(target)
