import pygame, sys, math

class Alert ():
    def __init__(self, startPos=[25,25], size =1):
        if size == 1:
            self.image = pygame.image.load("Skull.png")
        else:
            self.image = pygame.image.load("Skull"+str(size)+".png")
        self.rect = self.image.get_rect(center = startPos)
        self.kind = "endScreen"

    def update(self, size):
        pass
      
