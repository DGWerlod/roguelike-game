import pygame, constants
from logic import graphics
from objects.rect import Rect

pygame.init()

class Minimap(Rect):
    def __init__(self,floor):
        super().__init__(constants.gameW-210,10,100,80,constants.minigrey,None,[0,0],"map")
        self.contents = []
        self.xw = 12
        self.yw = 8
        self.gap = 5
        self.edgeGap = 10
        for y in range(constants.gridLength):
            self.contents.append([])
            for x in range(constants.gridLength):
                now = floor[y][x]
                if now != None:
                    self.contents[y].append(now["type"])
                else:
                    self.contents[y].append("none")

    def draw(self, ctx, curPos):
        graphics.round_rect(ctx,(self.x,self.y,self.w,self.h),self.color,10)
        y = self.y + self.edgeGap
        for row in range(len(self.contents)):
            x = self.x + self.edgeGap
            for col in range(len(self.contents)):
                nowColor = constants.black
                if curPos[0] == row and curPos[1] == col:
                    nowColor = constants.yellow
                elif self.contents[row][col] == "standard":
                    nowColor = constants.grey
                elif self.contents[row][col] == "shop":
                    nowColor = constants.green
                elif self.contents[row][col] == "dish":
                    nowColor = constants.blue
                elif self.contents[row][col] == "risk":
                    nowColor = constants.white
                elif self.contents[row][col] == "boss":
                    nowColor = constants.red
                graphics.round_rect(ctx,(x,y,self.xw,self.yw),nowColor,5)
                x += self.xw + self.gap
            y += self.yw + self.gap

    def go(self, ctx, curPos):
        self.draw(ctx, curPos)

    pygame.quit()
