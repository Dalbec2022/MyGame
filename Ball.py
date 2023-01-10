import pygame, sys, math

class Ball():
    def __init__(self, image, speed = [0,0], startPos=[0,0]):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(center = startPos)
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.rad = (self.rect.height/2 + self.rect.width/2)/2

        
        self.didBounceX = False
        self.didBounceY = False
        
        self.kind = "ball"

    def move(self):
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)

    def wallCollide(self, size):
        width = size[0]
        height = size[1]
        if not self.didBounceY:
            if self.rect.bottom > height:
                self.speedy = -self.speedy
                self.didBounceY = True
            if self.rect.top < 0:
                self.speedy = -self.speedy
                self.didBounceY = True
        if not self.didBounceY:
            if self.rect.right > width:
                self.speedx = -self.speedx 
                self.didBounceX = True
                
            if self.rect.left < 0:
                self.speedx = -self.speedx 
                self.didBounceX = True
            
    def ballCollide(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            if self.getDist(other) < self.rad + other.rad:
                                if not self.didBounceX:
                                    self.speedx = -self.speedx
                                    self.didBounceX = True
                                if not self.didBounceY:
                                    self.speedy = -self.speedy
                                    self.didBounceY = True
                            return True
        return False
        
    def wallTileCollide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        if not self.didBounceX:
                            self.speedx = -self.speedx
                            self.didBounceX = True
                        if not self.didBounceY:
                            self.speedy = -self.speedy
                            self.didBounceY = True
                        return True
        return False
                           
                           
                           
    def getDist(self, other):
        x1 = self.rect.centerx
        x2 = other.rect.centerx
        y1 = self.rect.centery
        y2 = other.rect.centery
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
                    

























