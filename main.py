from numpy.core.fromnumeric import var
from numpy.lib.function_base import gradient
from numpy.random.mtrand import f
import pygame
from pygame.locals import *
import random
import time

import matplotlib.pyplot as plt
import numpy as np

def main():
    from terrain import Terrain as Terrain
    from camera import Camera as Camera

    screen = pygame.display.set_mode((1080,720))
    movePer = 8
    while (True):
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                exit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            Camera.moveHoriz(-movePer)
        if keys[pygame.K_RIGHT]:
            Camera.moveHoriz(movePer)
        if keys[pygame.K_UP]:
            Camera.moveVert(-movePer)
        if keys[pygame.K_DOWN]:
            Camera.moveVert(movePer)
        
        Camera.draw(screen, Terrain)
        
        pygame.display.update()

        
        time.sleep(.001)

if __name__ == "__main__":
    main()