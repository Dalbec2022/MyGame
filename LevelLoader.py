import pygame, sys, math
from Wall import *
from Can import *
from Spawner import *

def loadLevel(lev):
    f = open(lev, 'r')
    lines = f.readlines()
    f.close()
    
    size = 50
    offset = size/2
    tiles = []
    cans = []
    walls = []
    spawners = []
    
    newLines = []
    for line in lines:
        newLine = ""
        for c in line:
            if c != "\n":
                newLine += c
        newLines += [newLine]
        
    lines = newLines
    
    
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "X":
                spawners += [Spawner([x*size+offset, y*size+offset])]
            if c == "#":
                walls += [Wall([x*size+offset, y*size+offset])]
    
    tiles = [walls, 
            cans, 
            spawners]            
    return tiles
                
    
#loadLevel("levels/1.lvl")

