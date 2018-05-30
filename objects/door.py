import pygame
from img import images
from objects.rect import Rect
pygame.init()

class Door(Rect):
    def __init__(self,x,y,w,h,type="rect",name="rect"):
        super().__init__(x,y,w,h,None,images.doors[type][name][0],[0,0],name)
        self.type = type
        self.open = False
    def go(self, ctx, state):
        if (state and not self.open):
            self.open = True
            self.img = images.doors[self.type][self.name][1]
        self.draw(ctx)

pygame.quit()
