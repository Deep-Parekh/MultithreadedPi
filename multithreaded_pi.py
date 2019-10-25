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
random.seed(time.time())
threads = []

def calculate_points(start, end):
    for i in range(start, end):
        x = random.uniform(0,1) 
        y = random.uniform(0,1)

        r = math.sqrt((x*x)+(y*y))

        if (r <= 1):
            lock.acquire()
            global totalCirclePoints
            totalCirclePoints += 1
            lock.release()

startTime = time.time()

for i in range(0,numThreads):
    if i == (numThreads-1):
        t = threading.Thread(target=calculate_points, args=(start,POINTS,))
    else:
        end = int(start + POINTS/numThreads)
        t = threading.Thread(target=calculate_points, args=(start,end,))
        threads.append(t)
        start = end
    t.start()

for i in range(0,len(threads)):
    threads[i].join()
pi = 4.0 * (float(totalCirclePoints)/POINTS)
totalTime = time.time() - startTime

print('It took %f seconds to estimate the value of pi' %totalTime)
print("The estimate is %f" %pi)
