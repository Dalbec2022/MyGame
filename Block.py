import pygame, sys, math

class Block():
    def __init__(self, startPos=[25,25], size =1):
        if size == 1:
            self.image = pygame.image.load("Glass.png")
        else:
            self.image = pygame.image.load("Wall"+str(size)+".png")
        self.rect = self.image.get_rect(topleft = startPos)
        self.kind = "wall"

    def update(self, size):
        pass
        

