import pygame, sys, math

class MyGameHud():
    def __init__(self, baseText, startPos=[0,10]):
        self.baseText = baseText
        self.font = pygame.font.Font(None, 48)
        self.image = self.font.render("Score: 0 ", 1 , (0, 0, 0))
        self.rect = self.image.get_rect(topleft = startPos)
        
    def update(self, score):
        text = self.baseText + str(score)
        self.image = self.font.render(text , 1 , (0, 0, 0))
        self.rect = self.image.get_rect(topleft = self.rect.topleft)
