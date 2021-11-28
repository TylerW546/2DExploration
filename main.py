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
        if keys[pygame.K_LEFT]:
            Player.moveLeft()
        if keys[pygame.K_RIGHT]:
            Player.moveRight()
        if keys[pygame.K_LSHIFT]:
            Player.speed = 5
        else:
            Player.speed = 2
        if Player.onGround:
            if keys[pygame.K_SPACE]:
                Player.jump()
        Player.update()
        
        Camera.followPlayer(Player)
        Camera.draw(screen, Terrain, Player)
        
        pygame.display.update()
        
        time.sleep(.01666)

if __name__ == "__main__":
    main()