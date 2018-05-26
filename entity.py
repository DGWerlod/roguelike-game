import pygame
pygame.init()

class Entity(object):
    def __init__(self,x,y,color,spd,name="none"):
        self.x = x
        self.y = y
        self.color = color
        self.spd = spd
        self.name = name
    def pos(): pass
    def draw(): pass
    def go():
        self.pos()
        self.draw()
