from main import * 

class Terrain():
    mapSize = (256,256)
    scale = 1

    terrainMap = np.zeros(mapSize, dtype=np.uint8)

    for col in range(len(terrainMap[0])):
        startHeight = random.randrange(mapSize[1]//4-2,mapSize[1]//4+2)
        for row in range(startHeight,len(terrainMap)):
            terrainMap[row][col] = 1

