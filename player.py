from numpy import e, vectorize
from Terrain import Terrain
from Vector2 import Vector2

class Player():
    x = 100
    y = 300
    playerWidth = 32
    playerHeight = 64

    width = playerWidth
    height = playerHeight

    pointEvery = 1
    sideCollide = [None for i in range(8)]
    onGround = False
    isJumping = False
    
    sprinting = False
    
    speed = None
    walkSpeed = 3
    runSpeed = 5
    airSpeed = 1.5
    
    
    waterSpeed = 1
    swimSpeed = 2
    

    airJumpMax = 10
    waterJumpMax = 3
    jumpFrame = 0
    jumpMax = 10

    jumpCool = 0
    jumpCoolMax = 0

    

    inWater = False
    touchWater = False
    wasSwimVertLastFrame = False
    swimVert = False
    swimHoriz = False

    velocity = Vector2(0,0)
    accell = Vector2(0,0)

    def update():
        if Player.sprinting:
            Player.speed = Player.runSpeed
        else:
            Player.speed = Player.walkSpeed
        
        Player.getSideCollides()
        Player.getTouchings()
        Player.checkWater()
        Player.jumpProcess()
        Player.fall()
        Player.move()
        Player.awayFromIntersect()
        Player.wasSwimVertLastFrame = Player.swimVert
        Player.swimVert = False

        Player.sprinting = False

        if Player.jumpCool > 0:
            Player.jumpCool -= 1

    def fall():
        if not Player.onGround:
            if not(Player.touchWater):
                Player.accell.y += 3
            else:
                Player.accell.y += .25
        else:
            Player.velocity.y = min(0,Player.velocity.y)
    
    def jump():
        if Player.onGround:
            if Player.jumpCool == 0:
                Player.isJumping = True
                Player.jumpFrame = Player.jumpMax
                Player.jumpCool = Player.jumpCoolMax

    def jumpProcess():
        if Player.isJumping == True:
            if Player.jumpFrame > 0:
                if not(Player.inWater):
                    Player.accell.y = -5
                else:
                    Player.accell.y = -3
                Player.jumpFrame -= 1
            else:
                Player.isJumping = False

    def checkWater():
        types = Player.rectBlockTypes(Player.x-Player.width//2,Player.y-Player.height//2-1,Player.width,Player.height,5)
        if 1 in types:
            Player.touchWater = True
        else:
            Player.touchWater = False

        allWater = True
        for type in types:
            if type != 1:
                allWater = False
                break
        if allWater:
            Player.inWater = True
            Player.jumpMax = Player.waterJumpMax
        else:
            Player.inWater = False
            Player.swimHoriz = False
            Player.jumpMax = Player.airJumpMax
            Player.hitBoxVert()

    def hitBoxHoriz():
        Player.width = Player.playerHeight
        Player.height = Player.playerWidth

    def hitBoxVert():
        Player.width = Player.playerWidth
        Player.height = Player.playerHeight

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
            Player.getTouchings()
            if not(Player.sideCollide[4]) or ignoreCollide:
                Player.y += 1
    
    def left(x, ignoreCollide = False):
        for i in range(x):
            Player.getTouchings()
            if not(Player.sideCollide[5]) or ignoreCollide:
                Player.x -= 1

    def up(x, ignoreCollide = False):
        for i in range(x):
            Player.getTouchings()
            if not(Player.sideCollide[6]) or ignoreCollide:
                Player.y -= 1

    def right(x, ignoreCollide = False):
        for i in range(x):
            Player.getTouchings()
            if not(Player.sideCollide[7]) or ignoreCollide:
                Player.x += 1
    
    def moveLeft():
        if Player.inWater:
            if Player.sprinting:
                Player.accell.x -= Player.swimSpeed
                Player.swimHoriz = True
                if not Player.swimVert:
                    Player.hitBoxHoriz()
            else:
                Player.accell.x -= Player.waterSpeed
        elif Player.onGround:
            Player.accell.x -= Player.speed
        else:
            Player.accell.x -= Player.airSpeed
        
    def moveRight():
        if Player.inWater:
            if Player.sprinting:
                Player.accell.x += Player.swimSpeed
                Player.swimHoriz = True
                if not Player.swimVert:
                    Player.hitBoxHoriz()
            else:
                Player.accell.x += Player.waterSpeed
        elif Player.onGround:
            Player.accell.x += Player.speed
        else:
            Player.accell.x += Player.airSpeed
    
    def moveDown():
        if Player.inWater:
            Player.accell.y += Player.waterSpeed
            if not Player.swimHoriz:
                Player.hitBoxVert()
            Player.swimVert = True
            Player.swimHoriz = False
    
    def moveUp():
        if Player.touchWater:
            Player.accell.y -= Player.waterSpeed
            if not Player.swimHoriz:
                Player.hitBoxVert()
            Player.swimVert = True
            Player.swimHoriz = False

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
        Player.sideCollide = [None for i in range(4)] + Player.sideCollide[4:]
        
        colliderStep = 5
        # Whether intersect is happening
        # Ground
        Player.sideCollide[0] = Player.rectCollider(Player.x-Player.width//2,Player.y+Player.height//2-1,Player.width,1,colliderStep)
        # Left
        Player.sideCollide[1] = Player.rectCollider(Player.x-Player.width//2,Player.y-Player.height//2,1,Player.height,colliderStep)
        # Head
        Player.sideCollide[2] = Player.rectCollider(Player.x-Player.width//2,Player.y-Player.height//2,Player.width,1,colliderStep)
        # Right
        Player.sideCollide[3] = Player.rectCollider(Player.x+Player.width//2-1,Player.y-Player.height//2,1,Player.height,colliderStep)
        
    def getTouchings():
        Player.sideCollide = Player.sideCollide[:4] + [None for i in range(4)]
        
        colliderStep = 5
        # Whether we are touching but not intersecting
        # GroundCheck
        Player.sideCollide[4] = Player.rectCollider(Player.x-Player.width//2,Player.y+Player.height//2,Player.width,1,colliderStep)
        # LeftWallCheck
        Player.sideCollide[5] = Player.rectCollider(Player.x-Player.width//2-1,Player.y-Player.height//2,1,Player.height,colliderStep)
        # UpperWallCheck
        Player.sideCollide[6] = Player.rectCollider(Player.x-Player.width//2,Player.y-Player.height//2-1,Player.width,1,colliderStep)
        # RightWallCheck
        Player.sideCollide[7] = Player.rectCollider(Player.x+Player.width//2,Player.y-Player.height//2,1,Player.height,colliderStep)
        
        # Ground
        if Player.sideCollide[4]:
            Player.onGround = True
        else:
            Player.onGround = False
    
    def rectBlockTypes(x,y,w,h,step):
        types = []
        ys = [y2 for y2 in range(y,y+h+1,step)] + [y+h]
        xs = [x2 for x2 in range(x,x+w+1,step)] + [x+w]
        for y2 in ys:
            for x2 in xs:
                types.append(Terrain.getBlockType(x2,y2))
        return types

    def rectCollider(x,y,w,h,step):
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
    