import pygame

class Camera():
    x = 5
    y = 5
    gridWorth = 16

    def moveHoriz(x):
        Camera.x += x

    def moveVert(y):
        Camera.y += y

    def draw(screen, Terrain):
        screen.fill((255,255,255))
        w,h = pygame.display.get_surface().get_size()
        for x in range(Camera.x-Camera.x%Camera.gridWorth, Camera.x+w, Camera.gridWorth):
            for y in range(Camera.y-Camera.y%Camera.gridWorth, Camera.y+h, Camera.gridWorth):
                if y//Camera.gridWorth >= 0 and y//Camera.gridWorth < len(Terrain.terrainMap) and x//Camera.gridWorth >= 0 and x//Camera.gridWorth < len(Terrain.terrainMap[0]):
                    if Terrain.terrainMap[y//Camera.gridWorth][x//Camera.gridWorth]==1:
                        pygame.draw.rect(screen, (0,0,0), (x-Camera.x,y-Camera.y,Camera.gridWorth,Camera.gridWorth))