from time import localtime
from time import strftime
from time import strptime
from time import sleep
from random import betavariate
from random import normalvariate
from datetime import datetime

class Entity(object):

    def __init__(self, name):
        self.name = name
        self.cache = []
        self.diffs = []
        #self.avg = avg
        #self.dist = dist

    def mention(self):
        tm = localtime()
        ptm = strftime("%Y-%m-%d %H:%M:%S", tm)
        #print(ptm)
        self.cache.append(ptm)

    def differences(self):
        for i in range(len(self.cache)):
            time1 = datetime.strptime(self.cache[i], "%Y-%m-%d %H:%M:%S") 
            try:
                time2 = datetime.strptime(self.cache[i+1],"%Y-%m-%d %H:%M:%S") 
                diff = time2-time1
                self.diffs.append(diff)
            except IndexError:
                pass
        return self.diffs

    def __str__(self):
        return self.name+": "+str(self.cache)

t1 = Entity("Hello")

while len(t1.cache) < 25:
    t1.mention()
    sleep(abs(normalvariate(5,5)))

print(t1.differences())
for t in t1.differences():
    print(t.total_seconds())
