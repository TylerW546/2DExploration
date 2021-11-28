from numpy import e, vectorize
from Terrain import Terrain
from Vector2 import Vector2

class Player():
    x = 100
    y = 300
    width = 32
    height = 64
    pointEvery = 1
    sideCollide = [False for i in range(4)]
    onGround = False
    isJumping = False
    
    jumpFrame = 0
    jumpMax = 10

    jumpCool = 0
    jumpCoolMax = 0

    speed = 3
    airSpeed = 1.5

    velocity = Vector2(0,0)
    accell = Vector2(0,0)

    def update():
        Player.getSideCollides()
        Player.jumpProcess()
        Player.fall()
        Player.move()
        Player.awayFromIntersect()

        if Player.jumpCool > 0:
            Player.jumpCool -= 1

    def fall():
        if not Player.onGround:
            Player.accell.y += 3
        else:
            Player.velocity.y = min(0,Player.velocity.y)
    
    def jump():
        if Player.jumpCool == 0:
            Player.isJumping = True
            Player.jumpFrame = Player.jumpMax
            Player.jumpCool = Player.jumpCoolMax

    def jumpProcess():
        if Player.isJumping == True:
            if Player.jumpFrame > 0:
                Player.accell.y = -5
                Player.jumpFrame -= 1
            else:
                Player.isJumping = False

    def move():
        Player.velocity.x += Player.accell.x
        Player.velocity.y += Player.accell.y
        Player.accell = Vector2()
        Player.velocity.ScalarMultipy(.9)
        if Player.onGround:
            Player.velocity.ScalarMultipy(.85)
        #Player.velocity[0] = max(-4, min(Player.velocity[0], 4))
        #Player.velocity[1] = max(-4, min(Player.velocity[1], 4))
        
        if Player.velocity.y > 0:
            Player.down(round(Player.velocity.y))
        elif Player.velocity.y < 0:
            Player.up(round(abs(Player.velocity.y)))
        
        if Player.velocity.x > 0:
            Player.right(round(Player.velocity.x))
        elif Player.velocity.x < 0:
            Player.left(round(abs(Player.velocity.x)))

    def down(x, ignoreCollide = False):
        for i in range(x):
            Player.getSideCollides()
            if not(Player.sideCollide[4]) or ignoreCollide:
                Player.y += 1
    
    def left(x, ignoreCollide = False):
        for i in range(x):
            Player.getSideCollides()
            if not(Player.sideCollide[5]) or ignoreCollide:
                Player.x -= 1

    def up(x, ignoreCollide = False):
        for i in range(x):
            Player.getSideCollides()
            if not(Player.sideCollide[6]) or ignoreCollide:
                Player.y -= 1

    def right(x, ignoreCollide = False):
        for i in range(x):
            Player.getSideCollides()
            if not(Player.sideCollide[7]) or ignoreCollide:
                Player.x += 1
    
    def moveLeft():
        if Player.onGround:
            Player.accell.x -= Player.speed
        else:
            Player.accell.x -= Player.airSpeed
        
    def moveRight():
        if Player.onGround:
            Player.accell.x += Player.speed
        else:
            Player.accell.x += Player.airSpeed

    def awayFromIntersect():
        Player.getSideCollides()
        if Player.sideCollide[0]:
            Player.y += -1
        else:
            if Player.sideCollide[2]:
                Player.y += 1
            if Player.sideCollide[1]:
                Player.x += 1
            if Player.sideCollide[3]:
                Player.x += -1

    def getSideCollides():
        Player.sideCollide = [None for i in range(8)]
        
        colliderStep = 5
        # Ground
        Player.sideCollide[0] = Player.colliderRect(Player.x-Player.width//2,Player.y+Player.height//2-1,Player.width,1,colliderStep)
        # Left
        Player.sideCollide[1] = Player.colliderRect(Player.x-Player.width//2,Player.y-Player.height//2,1,Player.height,colliderStep)
        # Head
        Player.sideCollide[2] = Player.colliderRect(Player.x-Player.width//2,Player.y-Player.height//2,Player.width,1,colliderStep)
        # Right
        Player.sideCollide[3] = Player.colliderRect(Player.x+Player.width//2-1,Player.y-Player.height//2,1,Player.height,colliderStep)
        # GroundCheck
        Player.sideCollide[4] = Player.colliderRect(Player.x-Player.width//2,Player.y+Player.height//2,Player.width,1,colliderStep)
        # LeftWallCheck
        Player.sideCollide[5] = Player.colliderRect(Player.x-Player.width//2-1,Player.y-Player.height//2,1,Player.height,colliderStep)
        # UpperWallCheck
        Player.sideCollide[6] = Player.colliderRect(Player.x-Player.width//2,Player.y-Player.height//2-1,Player.width,1,colliderStep)
        # RightWallCheck
        Player.sideCollide[7] = Player.colliderRect(Player.x+Player.width//2,Player.y-Player.height//2,1,Player.height,colliderStep)
        
        # Ground
        if Player.sideCollide[4]:
            Player.onGround = True
        else:
            Player.onGround = False
    
    def colliderRect(x,y,w,h,step):
        total = 0
        possible = 0
        ys = [y2 for y2 in range(y,y+h+1,step)] + [y+h]
        xs = [x2 for x2 in range(x,x+w+1,step)] + [x+w]
        for y2 in ys:
            for x2 in xs:
                possible += 1
                if Terrain.isCollider(x2,y2):
                    total += 1
        return total/possible
    