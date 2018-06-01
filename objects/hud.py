import pygame, constants, math
from img import images
from logic import graphics
from objects.rect import Rect

class HUD(Rect):
    def __init__(self, player):
        self.font = pygame.font.Font("fonts/muli.ttf",15)
        super().__init__(110,10,100,80,constants.minigrey,None,[0,0],"hud")
        self.stamps, self.stampsRECT = self.renderStamps(player)
        self.stampsLastFrame = player.stamps

    def renderStamps(self, player):
        stamps = self.font.render(str(player.stamps),True,constants.black)
        stampsRECT = stamps.get_rect()
        stampsRECT.right = 120 + 20
        stampsRECT.top = 40
        return stamps, stampsRECT

    def draw(self, ctx, player):
        peachCount = 0
        if player.hp >= 20:
            peachCount = math.ceil((player.hp-math.floor(player.hp/20)*20)/2)+2
        else:
            peachCount = math.ceil(player.hp/2)
        if peachCount < len(player.items):
            peachCount = len(player.items)
        graphics.round_rect(ctx,(self.x,self.y,20 + peachCount*15 + (peachCount-1)*5,self.h),self.color,10)

        location = self.x + 10
        tenPeachCount = 0
        if player.hp >= 20:
            ctx.blit(images.peach,(location,20))
            tenPeachCount = math.floor(player.hp/20)*10
            tenPeachText = self.font.render('x'+str(tenPeachCount),True,constants.black)
            tenPeachRECT = tenPeachText.get_rect()
            tenPeachRECT.right = 157
            tenPeachRECT.top = 20
            ctx.blit(tenPeachText,tenPeachRECT)
            location += 40
        for i in range(math.floor(player.hp/2) - tenPeachCount):
            ctx.blit(images.peach,(location,20))
            location += 20
        if player.hp % 2 == 1 and player.hp > 0:
            ctx.blit(images.halfPeach,(location,20))

        ctx.blit(images.foodStamp,(120,40))

        if player.stamps != self.stampsLastFrame:
            self.stamps, self.stampsRECT = self.renderStamps(player)
        ctx.blit(self.stamps,self.stampsRECT)
        self.stampsLastFrame = player.stamps

        location = self.x + 10
        for item in player.items:
            ctx.blit(pygame.transform.scale(images.icons[item.id]),(location,60))
            location += 20


    def go(self, ctx, player):
        self.draw(ctx, player)
