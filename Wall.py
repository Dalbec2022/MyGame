import pygame, sys, math

class Wall():
    def __init__(self, startPos=[25,25]):
        self.image = pygame.image.load("Wall.png")
        self.rect = self.image.get_rect(center = startPos)
        self.kind = "wall"

    def update(self, size):
        pass
        























