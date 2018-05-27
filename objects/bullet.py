import pygame, math
from logic import collisions
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

    def go(self, ctx, room, player):
        self.pos(room)
        self.draw(ctx)
        if self.name == "good":
            for e in room["enemies"]:
                if collisions.rectangles(self,e) and e.hp > 0:
                    self.removeFlag = True
                    e.hp -= self.dmg
        elif self.name == "bad":
            if collisions.rectangles(self,player):
                self.removeFlag = True
                player.hp -= self.dmg
