from numpy.core.fromnumeric import var
from numpy.lib.function_base import gradient
from numpy.random.mtrand import f
import pygame
from pygame.locals import *
import random
import time

import matplotlib.pyplot as plt
import numpy as np

mapSize = (256,256)
scale = 1

terrainMap = np.zeros(mapSize, dtype=np.uint8)

for col in range(len(terrainMap[0])):
    startHeight = random.randrange(mapSize[1]//4-2,mapSize[1]//4+2)
    for row in range(startHeight,len(terrainMap)):
        terrainMap[row][col] = 1

screen = pygame.display.set_mode((mapSize[0]*scale, mapSize[1]*scale))
screen.fill((255,255,255))
for i in range(len(terrainMap)):
    for j in range(len(terrainMap[0])):
        if terrainMap[j][i]==1:
            pygame.draw.rect(screen, (0,0,0), (i*scale,j*scale,scale,scale))

while (True):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()

    
    time.sleep(.001)
