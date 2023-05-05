import pygame, sys, math
from FireBall import *

class MasterChief(FireBall):
    def __init__(self, maxSpeed=4, startPos=[-350,100]):
        FireBall.__init__(self, "Master.png",  [0,0], startPos)
        self.rightimage = pygame.image.load("RightMaster.png")
        self.leftimage = pygame.image.load("leftMaster.png")
        self.maxSpeed=maxSpeed
        self.kind = "player"
        
        self.gravity = 0.5
        self.jumping = True
        self.jumpPower = 20
        
        self.spawnsound = pygame.mixer.Sound("Sounds/Spawn.ogg")
        self.walkingsound = pygame.mixer.Sound("Sounds/Walking.ogg")
        self.spawnsound.play()
        
        #self.moveSound = pygame.mixer.Sound(fullname)
        
    def update(self,size):            
        self.move()
        return self.wallCollide(size)
        
    def move(self):
        self.speedy += self.gravity
        self.didBounceX = False
        self.didBounceY = False
        if self.speedx != 0:
            self.walkingsound.play()
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        #if speedx != 0:
        #    self.moveSound.play()

        
    def goKey(self, direction):
        if direction == "left":
            self.speedx = -self.maxSpeed
            self.image=self.leftimage
        elif direction == "right":
            self.speedx = self.maxSpeed
            self.image=self.rightimage
            
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
                return"bottom"
            if self.rect.top < 0:
                return"top"
        if not self.didBounceX:
            if self.rect.right > width:
                return"right"
            if self.rect.left < 0:
                return"left"
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
