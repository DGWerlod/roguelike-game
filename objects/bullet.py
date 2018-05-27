import pygame, math
from objects.rect import Rect
pygame.init()

class Bullet(Rect):
    def __init__(self,x,y,w,h,img,angle,dmg,name="bullet"):
        spdX = 8*math.cos(angle)
        spdY = 8*math.sin(angle)
        super().__init__(x,y,w,h,None,img,[spdX,spdY],name)
        self.removeFlag = False
        self.dmg = dmg

    def pos(self, room):
        self.x += self.spd[0]
        self.y += self.spd[1]
        if not self.canMove(room):
            self.removeFlag = True

    def go(self, ctx, room):
        self.pos(room)
        self.draw(ctx)
