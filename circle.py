import pygame, entity
pygame.init()

class Circle(entity.Entity):
    def __init__(self,x,y,r,color,spd,name="none"):
        super().__init__(x,y,color,spd,name)
        self.r = r
    def draw(self):
        pygame.draw.circle(ctx,self.color,(self.x,self.y),self.r)
