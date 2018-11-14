import pygame, math, constants
from img import images
from sound import sounds
from controls import keyboard, mouse
from objects.bullet import Bullet
from objects.actor import Actor

class Player(Actor):
    
    startValues = [170, 240, 10, [5, 5], 1, 15]
    FACE_LEFT = 0
    FACE_RIGHT = 1
    
    def __init__(self):
        super().__init__(self.startValues[0],self.startValues[1],constants.playerW,constants.playerH,
                        None,[images.playerLeft,images.playerRight],self.startValues[2],self.startValues[3],"player")
        self.dmg = self.startValues[4]
        self.stamps = 0
        self.items = []
        self.face = self.FACE_RIGHT
        self.atkSpd = self.startValues[5]
        self.attackCD = 0

    def getFeet(self):
        return pygame.Rect(self.x,self.y + self.h/2,self.w,self.h/2)

    def pos(self, room):
        if keyboard.controls['keyW'] is True:
            self.y -= self.spd[1]
            while not super().canMove(room):
                self.y += 1
        if keyboard.controls['keyA'] is True:
            self.face = self.FACE_LEFT
            self.x -= self.spd[0]
            while not super().canMove(room):
                self.x += 1
        if keyboard.controls['keyS'] is True:
            self.y += self.spd[1]
            while not super().canMove(room):
                self.y -= 1
        if keyboard.controls['keyD'] is True:
            self.face = self.FACE_RIGHT
            self.x += self.spd[0]
            while not super().canMove(room):
                self.x -= 1

    def attack(self):
        sounds.play("chop")
        selfCenterX = self.x + self.w/2
        selfCenterY = self.y + self.h/2
        theta = math.atan2(mouse.mouse['pos'][1]-selfCenterY, mouse.mouse['pos'][0]-selfCenterX)
        return Bullet(selfCenterX-5,selfCenterY-5,10,10,images.frenchFry,theta,self.dmg,"good")

    def draw(self, ctx):
        ctx.blit(self.img[math.floor(self.face)], (self.x,self.y))

    def go(self, ctx, room):
        super().go(ctx, room)
        if self.attackCD > 0:
            self.attackCD -= 1
        elif mouse.mouse['held'] is not 0:
            self.attackCD = self.atkSpd
            return self.attack()
        return None
