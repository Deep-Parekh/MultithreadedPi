import threading
import random
import os
import math
import time

startTime = time.time()
POINTS = 1000000
totalCirclePoints = 0
totalTime = 0
pi = 0

def calculatePoints(pointsArray, start, end):
    circlePoints = 0
    for i in range(start, end):
        x = random.uniform(0,1) 
        y = random.uniform(0,1)

        r = math.sqrt((x*x)+(y*y))
        if (r <= 1):
            circlePoints += 1

    return circlePoints   