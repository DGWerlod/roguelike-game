import pygame, constants
from img import images
from objects.rect import Rect

class Door(Rect):
    def __init__(self,type,name):
        if name == "a" or name == "d":
            y = constants.LRDoor
            w = constants.doorSlim
            h = constants.doorWide
            if name == "a":
                x = 0
            else:
                x = constants.gameW-constants.doorSlim
        else: # w or s
            x = constants.TBDoor
            w = constants.doorWide
            h = constants.doorSlim
            if name == "w":
                y = 0
            else:
                y = constants.gameH-constants.doorSlim
        super().__init__(x,y,w,h,None,images.doors[type][name][0],[0,0],name)
        self.type = type
        self.open = False
    def go(self, ctx, state):
        if (state and not self.open):
            self.open = True
            self.img = images.doors[self.type][self.name][1]
        self.draw(ctx)
