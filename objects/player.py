import pygame, math, constants
from img import images
from sound import sounds
from controls import keyboard, mouse
from objects.bullet import Bullet
from objects.actor import Actor

startValues = [170,240,10,[5,5],1,15]

class Player(Actor):
    def __init__(self):
        super().__init__(startValues[0],startValues[1],constants.playerW,constants.playerH,
                        None,[images.player1,images.player2],startValues[2],startValues[3],"player")
        self.dmg = startValues[4]
        self.stamps = 0
        self.items = []
        self.phase = 0
        self.atkSpd = startValues[5]
        self.attackCD = 0

    def getFeet(self):
        return pygame.Rect(self.x,self.y + self.h/2,self.w,self.h/2)

    def pos(self, room):
        if keyboard.controls['keyW'] == True:
            self.y -= self.spd[1]
            while not super().canMove(room):
                self.y += 1
        if keyboard.controls['keyA'] == True:
            self.x -= self.spd[0]
            while not super().canMove(room):
                self.x += 1
        if keyboard.controls['keyS'] == True:
            self.y += self.spd[1]
            while not super().canMove(room):
                self.y -= 1
        if keyboard.controls['keyD'] == True:
            self.x += self.spd[0]
            while not super().canMove(room):
                self.x -= 1

    def animate(self):
        self.phase += 1
        if self.phase == 60:
            self.phase = 0

    def attack(self):
        sounds.play("chop")
        selfCenterX = self.x + self.w/2
        selfCenterY = self.y + self.h/2
        theta = math.atan2(mouse.mouse['pos'][1]-selfCenterY, mouse.mouse['pos'][0]-selfCenterX)
        return Bullet(selfCenterX-5,selfCenterY-5,10,10,images.frenchFry,theta,self.dmg,"good")

    def draw(self, ctx):
        self.animate()
        ctx.blit(self.img[math.floor(self.phase/30)], (self.x,self.y))

    def go(self, ctx, room):
        super().go(ctx, room)
        if self.attackCD > 0:
            self.attackCD -= 1
        elif mouse.mouse['held'] == True:
            self.attackCD = self.atkSpd
            return self.attack()
        return None
