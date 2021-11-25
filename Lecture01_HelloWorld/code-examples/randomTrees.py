from turtle import *


import random

def treeRandom(trunkLen, minLength, thickness, minThickness, 
               minAngle, maxAngle, minShrink, maxShrink):
    
    if (trunkLen < minLength) or (thickness < minThickness): # Base case
        pass # Do nothing
    else:
        angle1 = random.uniform(minAngle, maxAngle)
        angle2 = random.uniform(minAngle, maxAngle)
        shrink1 = random.uniform(minShrink, maxShrink)
        shrink2 = random.uniform(minShrink, maxShrink)
        pensize(thickness)
        fd(trunkLen)
        rt(angle1)
        treeRandom(trunkLen*shrink1, minLength, thickness*shrink1,
                   minThickness, minAngle, maxAngle, minShrink, maxShrink)
        lt(angle1 + angle2)
        treeRandom(trunkLen*shrink2, minLength, thickness*shrink2, 
                   minThickness, minAngle, maxAngle, minShrink, maxShrink)
        rt(angle2)
        pensize(thickness)
        bk(trunkLen)




if __name__ == '__main__':
    reset()
    speed(0)
    lt(90) # Face north first to grow the tree upwards
    treeRandom(120, 3, 20, 1, 15, 55, 0.5, 0.8) 
    getscreen().getcanvas().postscript(file="randomTree1.eps")
