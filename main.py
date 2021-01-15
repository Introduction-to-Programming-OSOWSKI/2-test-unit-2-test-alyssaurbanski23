def waterState(x, y, z):
    if x == 10:
        return solid
    elif y == 60:
        return liquid
    else:
        return gas

print(waterState( 10, 60, 419))


def isDozen(x, y):
    if x / y:
        return True 
    
    else:
        return False

print(isDozen(9, 3))

def toGerman(x):
    if x == ja:
        return True
    else:
        return False

print(toGerman(ja))


def stopLight(x, y, z):
    if x == go:
        return green
    elif y == slowdown:
        return yellow
    else:
        return red

print(stopLights(go, slowdown, stop))
