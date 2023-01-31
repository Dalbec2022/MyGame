import pygame, sys, math

class Can():
    def __init__(self, startPos=[25,25]):
        self.image = pygame.image.load("Can.png")
        self.rect = self.image.get_rect(center = startPos)
        self.rad = self.rect.width/2
        self.kind = "can"

    def update(self, size):
        pass
