import pygame, sys, math
from FireBall import *

class MasterChief(FireBall):
    def __init__(self, maxSpeed=4, startPos=[-350,100]):
        FireBall.__init__(self, "Master.png",  [0,0], startPos)
        self.maxSpeed=maxSpeed
        self.kind = "player"
        
        self.gravity = 1
        self.jumping = True
        self.jumpPower = 30
        
    def update(self,size):            
        self.move()
        return self.wallCollide(size)
        
    def move(self):
        self.speedy += self.gravity
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)

        
    def goKey(self, direction):
        if direction == "left":
            self.speedx = -self.maxSpeed
        elif direction == "right":
            self.speedx = self.maxSpeed
        elif direction == "jump":
            if not self.jumping:
                self.speedy = -self.jumpPower
                self.move()
                self.jumping = True
        elif direction == "down":
            self.speedy = self.maxSpeed
        elif direction == "sleft":
            self.speedx = 0
        elif direction == "sright":
            self.speedx = 0
        elif direction == "sup":
            self.speedy = 0
        elif direction == "sdown":
            self.speedy = 0
            
    def wallCollide(self, size):
        width = size[0]
        height = size[1]
        if not self.didBounceY:
            if self.rect.bottom > height:
                self.speedy = -self.speedy
                self.move()
                self.speedy = 0
                self.didBounceY = True
                return"bottom"
            if self.rect.top < 0:
                self.speedy = -self.speedy
                self.move()
                self.speedy = 0
                self.didBounceY = True
                return"bottom"
                
        if not self.didBounceX:
            if self.rect.right > width:
                self.speedx = -self.speedx
                self.move()
                self.speedx = 0
                self.didBounceX = True
                return"bottom"
            if self.rect.left < 0:
                self.speedx = -self.speedx 
                self.move()
                self.speedx = 0
                self.didBounceX = True
                return"bottom"
        return"none"
            
    def objectCollide(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            if self.getDist(other) < self.rad + other.rad:
                                return True
        return False
        
    def wallTileCollide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        xdiff = self.rect.centerx - other.rect.centerx
                        ydiff = self.rect.centery - other.rect.centery
                        print(xdiff,ydiff)
                        if abs(xdiff) > abs(ydiff):    #Left/Right collsion
                            if xdiff < 0:
                                self.rect.right = other.rect.left-1
                                print("\t==============hit left")
                            elif xdiff > 0:
                                self.rect.left = other.rect.right+1
                                print("\t==============hit right")
                        else:                           #Up/Down collsions
                            if ydiff <0:
                                #print(self.rect.bottom, other.rect.top)
                                self.rect.bottom = other.rect.top-1
                                self.speedy = 0
                                self.jumping = False
                                print("\thit top")
                            elif ydiff>0:
                                self.rect.top = other.rect.bottom + 1
                                self.speedy = 0
                                print("\t============hit bottom")
                        return True
        return False
                        
    def getDist(self, other):
        x1 = self.rect.centerx
        x2 = other.rect.centerx
        y1 = self.rect.centery
        y2 = other.rect.centery
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)