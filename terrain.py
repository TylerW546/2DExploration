from random import randrange
from Vector2 import Vector2
from main import * 
import math

class Perlin():
    def interpolate(pa, pb, px):
        ft = px * 3.141593
        f = (1 - math.cos(ft)) * 0.5
        return pa * (1 - f) + pb * f
    
    def interpolateTwo(pa, pb, px):
        return pa * (1 - px) + pb * px

    def __init__(self, amp = 100, wl = 100, w = 100, h = 100, fq = 1/100):
        self.x = 0
        self.yStart = 0
        self.y = self.yStart 
        
        self.w = w
        self.h = h
        
        self.amp = amp # amplitude
        self.wl = wl # wavelength
        self.fq = fq # frequency
        
        self.M = 4294967296 # a - 1 should be divisible by m's prime factors
        self.A = 166452 #c and m should be co-prime
        self.C = 1
        
        self.Z = math.floor(random.randrange(1000)/1000 * self.M)
                
        self.a = self.rand()
        self.b = self.rand()
    
    def rand(self):
        self.Z = (self.A * self.Z + self.C) % self.M
        return self.Z / self.M
    
    def create(self):
        heights = []
        while(self.x < self.w):
            if (self.x % self.wl == 0):
                self.a = self.b
                self.b = self.rand()
                self.y = self.yStart + self.a * self.amp
            else:
                self.y = self.yStart + Perlin.interpolate(self.a, self.b, (self.x % self.wl) / self.wl) * self.amp
            heights.append(self.y)
            self.x += 1
        return heights
    
    #octave generator
    def GenerateNoise(amp, wl, octaves, divisor, width):
        result = []
        for i in range(octaves):
            result.append(Perlin(amp, wl, width).create())
            amp /= divisor
            wl /= divisor
        return result

    #combines octaves together
    def CombineNoise(resultsList):
        final = []
        for index in range(len(resultsList[0])):
            total = 0.0
            for list in range(len(resultsList)):
                total += resultsList[list][index]
            final.append(total)
        return final
            


class Terrain():
    mapSize = (256,1000)
    gridWorth = 33

    terrainMap = np.zeros(mapSize, dtype=np.uint8)

    octaves = 4
    heights = Perlin.CombineNoise(Perlin.GenerateNoise(128,128,octaves,2,mapSize[1]))
    firstHeight = mapSize[0]-round(heights[5])
    
    for col in range(len(terrainMap[0])):
        startHeight = heights[col]
        for row in range(mapSize[0]-round(startHeight),len(terrainMap)):
            terrainMap[row][col] = 1
    
    plt.imshow(terrainMap)
    plt.show()
    
    def isCollider(x, y):
        if y//Terrain.gridWorth >= 0 and y//Terrain.gridWorth < len(Terrain.terrainMap) and x//Terrain.gridWorth >= 0 and x//Terrain.gridWorth < len(Terrain.terrainMap[0]):
            if Terrain.terrainMap[y//Terrain.gridWorth][x//Terrain.gridWorth]==1:
                return True
        return False
    
    def getIndexes(x,y):
        return y//Terrain.gridWorth, x//Terrain.gridWorth
