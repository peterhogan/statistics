import random
from time import sleep

def randomWalk(x, update=True):
  countx = 0
  county = 0
  runs = 0
  while runs < x:
    if random.normalvariate(0,10) > 0:
      countx += 1
    else:
      countx -= 1

    if random.normalvariate(0,10) > 0:
      county += 1
    else:
      county -= 1
    
    if update == True:
      print([countx,county])#, end='\n')#, flush=True)
      sleep(0.2)
    
    runs += 1
  
  return [countx,county]

def randomWalkMean(x,y):
  
  randomwalks = []
  for i in range(x):
    randomwalks.append(randomWalk(y, update=False))
  
  return sum(randomwalks)/len(randomwalks)

