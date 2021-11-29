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
    from Terrain import Terrain as Terrain
    from player import Player as Player
    from camera import Camera as Camera
    Player.x = 5*Terrain.gridWorth
    Player.y = Terrain.firstHeight*Terrain.gridWorth
    
    screen = pygame.display.set_mode((1080,720))
    while (True):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT]:
            Player.sprinting = True
        if keys[pygame.K_w]:
            Player.moveUp()
        if keys[pygame.K_a]:
            Player.moveLeft()
        if keys[pygame.K_s]:
            Player.moveDown()
        if keys[pygame.K_d]:
            Player.moveRight()
        if keys[pygame.K_SPACE]:
            Player.jump()
        Player.update()
        
        Camera.followPlayer(Player)
        Camera.draw(screen, Terrain, Player)
        
        pygame.display.update()
        
        time.sleep(.01666)

if __name__ == "__main__":
    main()