import pygame, sys, math
from Block import *
from Spawner import *

def loadScreen(scn):
    f = open(scn, 'r')
    lines = f.readlines()
    f.close()
    
    size = 50
    offset = 0
    tiles = []
    blocks = []
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
                blocks += [Block([x*size+offset, y*size+offset])]
            if c == "_":
                blocks += [Block([x*size+offset, y*size+offset], 37)]
    
    tiles = [blocks, 
            spawners]            
    return tiles
                
    
loadScreen("screens/1.scn")


