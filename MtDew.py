import pygame, sys, math

class Can():
    def __init__(self, startPos=[25,25], size =1):
        if size == 1:
            self.image = pygame.image.load("can.png")
        else:
            self.image = pygame.image.load("Can"+str(size)+".png")
        self.rect = self.image.get_rect(topleft = startPos)
        self.rad = self.rect.width/2
        self.kind = "can"

    def update(self, size):
        pass
