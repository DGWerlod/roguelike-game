import pygame
pygame.init()

class Entity(object):
    def __init__(self,x,y,color,spd,name="none"):
        self.x = x
        self.firstX = x
        self.y = y
        self.firstY = y
        self.color = color
        self.spd = spd
        self.firstSpd = spd
        self.name = name
    def pos(self): pass
    def draw(self, ctx): pass
    def go(self, ctx):
        self.pos()
        self.draw(ctx)
