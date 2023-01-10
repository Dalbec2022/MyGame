import pygame, sys, math, random
from FireBall import * 

class Spawner():
    def __init__(self, startPos=[25,25]):
        self.image = pygame.image.load("Spawner.png")
        self.rect = self.image.get_rect(topleft = startPos)
        self.kind = "spawner"
        
        self.spawnTimer = random.randint(0,60*1)
        self.spawnTimerMax = 60*5

    def update(self, size):
        self.spawnTimer += 1
        if self.spawnTimer >= self.spawnTimerMax:
            self.spawnTimer = 0
            return True
        else:
            return False
            
    def spawn(self):
        speed = [0,0]
        while speed == [0,0]:
            speed = [random.randint(-7,7), random.randint(-7,7)]
        return FireBall("ball.png", 
               speed,
               self.rect.center)
        























