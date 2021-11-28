import pygame
from player import Player as Player

class Camera():
    x = 5
    y = 5

    def followPlayer(Player):
        Camera.x = Player.x - 500
        Camera.y = Player.y - 300
        
    def moveHoriz(x):
        Camera.x += x

    def moveVert(y):
        Camera.y += y

    def draw(screen, Terrain, Player):
        screen.fill((178,255,255))
        w,h = pygame.display.get_surface().get_size()
        
        # Terrain
        for x in range(Camera.x-Camera.x%Terrain.gridWorth, Camera.x+w, Terrain.gridWorth):
            for y in range(Camera.y-Camera.y%Terrain.gridWorth, Camera.y+h, Terrain.gridWorth):
                if y//Terrain.gridWorth >= 0 and y//Terrain.gridWorth < len(Terrain.terrainMap) and x//Terrain.gridWorth >= 0 and x//Terrain.gridWorth < len(Terrain.terrainMap[0]):
                    code = Terrain.terrainMap[y//Terrain.gridWorth][x//Terrain.gridWorth]
                    if code != 0:
                        pygame.draw.rect(screen, Terrain.colors[code], (x-Camera.x,y-Camera.y,Terrain.gridWorth,Terrain.gridWorth))

        # Player
        pygame.draw.rect(screen, (255,0,0), (Player.x-Player.width//2-Camera.x, Player.y-Player.height//2-Camera.y,Player.width+1,Player.height+1))