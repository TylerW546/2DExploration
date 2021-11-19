from random import randrange
from Vector2 import Vector2
from main import * 
import math

class Perlin():
    def fade(t):
        return t*t*t*(t*(t*6.0 - 15.0) + 10.0)
    
    def grad(p):
        texture_width = 256.0
        v = random.randrange(10)
        if v > 5:
            return 1.0
        else: 
            return -1.0

    def noise(p):
        p0 = float(math.floor(p))
        p1 = p0 + 1.0
            
        t = p - p0
        fade_t = Perlin.fade(t)

        g0 = Perlin.grad(p0)
        g1 = Perlin.grad(p1)
  
        return (1.0-fade_t)*g0*(p - p0) + fade_t*g1*(p - p1)
    
    def pixelValue(coord, screenSize):
        frequency = 1.0 / 20.0
        amplitude = 1.0 / 5.0
        n = Perlin.noise(coord.x * frequency) * amplitude
        y = 2.0 * ((screenSize.y-coord.y)/screenSize.y) - 1.0; # map coord.y into [-1; 1] range
        if n > y: 
            return 1
        else:
            return 0

print(Perlin.noise(2014))

class Terrain():
    mapSize = (256,256)
    gridWorth = 9

    terrainMap = np.zeros(mapSize, dtype=np.uint8)

    for col in range(len(terrainMap[0])):
        startHeight = random.randrange(mapSize[1]//4-1,mapSize[1]//4+1)
        for row in range(startHeight,len(terrainMap)):
            terrainMap[row][col] = 1
    for i in range(len(terrainMap)):
        for j in range(len(terrainMap[i])):
            terrainMap[i][j] = Perlin.pixelValue(Vector2(j,i), Vector2(len(terrainMap[0]), len(terrainMap)))
    
    def isCollider(x, y):
        if y//Terrain.gridWorth >= 0 and y//Terrain.gridWorth < len(Terrain.terrainMap) and x//Terrain.gridWorth >= 0 and x//Terrain.gridWorth < len(Terrain.terrainMap[0]):
            if Terrain.terrainMap[y//Terrain.gridWorth][x//Terrain.gridWorth]==1:
                return True
        return False
    
    def getIndexes(x,y):
        return y//Terrain.gridWorth, x//Terrain.gridWorth
