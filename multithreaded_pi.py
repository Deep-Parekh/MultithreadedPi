import threading
import random
import os
import math
import time
import sys

numThreads = int(sys.argv[1])
POINTS = int(sys.argv[2])
if (POINTS < numThreads):
    numThreads = POINTS
totalCirclePoints = 0
totalTime = 0
pi = 0
start = 0
lock = threading.Lock()
startTime = time.time()

for i in range(0,numThreads):
    if i == (numThreads-1):
        t = threading.Thread(target=calculatePoints, args=(start,POINTS))
    else:
        end = start + POINTS/numThreads
        t = threading.Thread(target=calculatePoints, args=(start,end))
        start = end
    t.start()

pi = float(totalCirclePoints)/POINTS
totalTime = startTime - time.time()

print("It took " + totalTime + " seconds to estimate the value of pi")
print("The estimate is " + pi)

def calculatePoints(start, end):
    circlePoints = 0
    for i in range(start, end):
        x = random.uniform(0,1) 
        y = random.uniform(0,1)

        r = math.sqrt((x*x)+(y*y))

        if (r <= 1):
            lock.acquire()
            totalCirclePoints += 1
            lock.release()