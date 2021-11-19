import math

def distance(x1,y1, x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

class Vector2(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def Add(self, other):
        self.x += other.x
        self.y += other.y
    
    def Subtract(self, other):
        self.x -= other.x
        self.y -= other.y
    
    def Magnitude(self):
        return distance(0,0,self.x,self.y)

    def ScalarMultipy(self, factor):
        self.x *= factor
        self.y *= factor

    def Normalize(self, dist):
        factor = dist/self.Magnitude()
        self.ScalarMultipy(factor)
    