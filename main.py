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

    screen = pygame.display.set_mode((1080,720))
    movePer = 1
    while (True):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            Player.moveHoriz(-movePer)
        if keys[pygame.K_RIGHT]:
            Player.moveHoriz(movePer)
        if Player.onGround:
            if keys[pygame.K_UP]:
                Player.jump()
        if keys[pygame.K_DOWN]:
            Player.moveVert(movePer)
        
        if True in Player.sideCollide:
            print(Player.sideCollide)
        Player.update()
        
        Camera.followPlayer(Player)
        Camera.draw(screen, Terrain, Player)
        
        pygame.display.update()

        
        time.sleep(.001)

if __name__ == "__main__":
    main()