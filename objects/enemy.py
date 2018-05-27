import pygame
from objects.actor import Actor
from img import images
pygame.init()

class Enemy(Actor):
    def __init__(self,x,y,w,h,color,maxHP,atkSpd,dmg,name="enemy",spd=[0,0]):
        super().__init__(x,y,w,h,color,None,maxHP,spd,name)
        self.atkSpd = atkSpd
        self.attackCD = atkSpd
        self.dmg = dmg

    def attack(self):
        pass

    def draw(self, ctx):
        ctx.blit(images.getImage(self.name),(self.x,self.y))

    def go(self, ctx, room):
        if self.hp<=0:
            super().go(ctx,room)
            if self.attackCD > 0:
                self.attackCD -= 1
                return None
            else:
                return self.attack()
