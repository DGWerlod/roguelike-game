import pygame
from logic import collisions
from img import images
from objects.rect import Rect
pygame.init()

class Item(Rect):
    def __init__(self,id,x,y,w,h,spd=[0,0],name="item"):
        super().__init__(x,y,w,h,None,None,spd,name)
        self.id = id
        self.consumedFlag = False
    def activate(self, target):
        if self.id == 0: # peach
            if target.hp + 2 > target.maxHP:
                target.hp = target.maxHP
            else:
                target.hp += 2
        elif self.id == 1: # knife
            target.dmg += 1
        elif self.id == 2: # basil
            pass
        elif self.id == 3: # paprika
            if target.atkSpd > 5:
                target.atkSpd -= 2
            else:
                target.spd += 1
        elif self.id == 4: # pepper
            target.spd += 1
        elif self.id == 5: # salt
            pass
        elif self.id == 6: # tumeric
            pass
        elif self.id == 7: # giant-peach
            target.maxHP += 2
        elif self.id == 8: #
            pass
        elif self.id == 9: #
            pass
        self.consumedFlag = True
    def draw(self, ctx):
        if not self.consumedFlag:
            ctx.blit(images.items[self.id],(self.x,self.y))
    def go(self, ctx, player):
        super().go(ctx)
        if collisions.rectangles(self, player) and not self.consumedFlag:
            self.activate(player)
