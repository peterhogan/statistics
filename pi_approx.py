from numpy.random import uniform
from time import time

def inSphere(point, centre, radius):
    if len(point) != len(centre):
        raise  KeyError("dimension of point does not match dimension of centre")
    circle = sum([(point[i] - centre[i])**2 for i in range(len(point))])
    boundary = radius**2
    if circle < boundary:
        return True
    return False

inCirc = []
outCirc = []

start = time()
iterations = 1E7

for i in range(1,int(iterations)):
    point = [uniform(low=0.0, high=1.0),uniform(low=0.0, high=1.0)]
    if inSphere(point, [0,0],1):
        inCirc.append(point)
    else:
        outCirc.append(point)
    if i % 100 == 0:
        prog = i/int(iterations)
        itertime = time() - start
        timeleft = (1-prog)*itertime
        print(" Complete:\t",str(round(100*prog, 2))+"%\t","\tseconds left:\t",round((int(iterations)/i-1)*itertime), end="\r", flush=True)
print("")

print("time taken:",time() - start)
print("points in circle =",len(inCirc))
print("points outside circle =",len(outCirc))
print("ratio:",4*len(inCirc)/int(iterations))
