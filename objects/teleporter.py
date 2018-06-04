import pygame
import constants
from img import images
from objects.rect import Rect

class Teleporter(Rect):
    def __init__(self):
        super().__init__((constants.gameW-80)/2,(constants.gameH-80)/2,80,80,None,images.teleporter,None,"teleporter")

    def getRect(self):
        return pygame.Rect(self.x,self.y,self.w,self.h)

    def go(self, ctx, player):
        super().go(ctx)
        return pygame.Rect(self.getRect()).contains(player.getFeet())
