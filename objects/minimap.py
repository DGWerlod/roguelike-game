import constants
from logic import graphics, collisions
from controls.mouse import mouse
from objects.rect import Rect

colors = {
    "standard": constants.grey,
    "shop": constants.green,
    "dish": constants.blue,
    "risk": constants.white,
    "boss": constants.red,
    "player": constants.yellow
}

class Minimap(Rect):
    def __init__(self,floor,level):
        super().__init__(constants.gameW - 210, 10, 100, 80, constants.miniGrey, None, [0, 0], "map")
        self.contents = []
        self.xw = 12
        self.yw = 8
        self.gap = 5
        self.edgeGap = 10
        self.level = level
        for y in range(constants.gridLength):
            self.contents.append([])
            for x in range(constants.gridLength):
                now = floor[y][x]
                if now is not None:
                    self.contents[y].append(colors[now.type])
                else:
                    self.contents[y].append(None)

    def draw(self, ctx, curPos):
        graphics.round_rect(ctx,(self.x,self.y,self.w,self.h),self.color,10)
        y = self.y + self.edgeGap
        for row in range(len(self.contents)):
            x = self.x + self.edgeGap
            for col in range(len(self.contents)):
                if curPos[0] == row and curPos[1] == col:
                    graphics.round_rect(ctx,(x,y,self.xw,self.yw),colors["player"],5)
                elif self.contents[row][col] is not None:
                    graphics.round_rect(ctx,(x,y,self.xw,self.yw),self.contents[row][col],5)
                x += self.xw + self.gap
            y += self.yw + self.gap

        if collisions.rectPoint(self, mouse["pos"]):
            levelText = constants.muli["20"].render("Floor " + str(self.level),True,constants.black)
            levelRECT = levelText.get_rect()
            levelRECT.centerx = mouse["pos"][0]
            levelRECT.top = 97
            graphics.round_rect(ctx,(levelRECT.left-5,100,levelRECT.width+10,levelRECT.height),self.color,10)
            ctx.blit(levelText,levelRECT)

    def go(self, ctx, curPos):
        self.draw(ctx, curPos)
