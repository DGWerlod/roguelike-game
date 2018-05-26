import pygame
from objects.rect import Rect
import constants
from logic import collisions


pygame.init()

class Actor(Rect):
    def __init__(self,x,y,w,h,color,img,maxHP,spd=[0,0],name="actor"):
        super().__init__(x,y,w,h,color,spd,name)
        self.img = img
        self.maxHP = maxHP
        self.hp = maxHP

    def act(self): pass

    def canMove(self):
        """
        for o in obstructions:
            if collision.rectangles(self,o):
                return False
        """
        return True


    def pos(self):
        if self.canMove():
            self.x += self.spd[0]
            self.y += self.spd[1]

        # Revert if outside game boundary
        if self.x < 0 or self.x + self.w > constants.gameW:
            self.x -= self.spd[0]
        if self.y < 0 or self.y + self.h > constants.gameH:
            self.y -= self.spd[1]

    def draw(self, ctx):
        ctx.blit(self.img, (self.x,self.y))
