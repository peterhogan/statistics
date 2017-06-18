from time import localtime
from time import strftime
from time import strptime
from time import sleep
from random import betavariate
from random import normalvariate
from datetime import datetime
from scipy.stats import norm,gamma
from numpy import linspace
from pylab import plot,show,hist,figure,title

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
                self.diffs.append(diff.total_seconds())
            except IndexError:
                pass
        return self.diffs

    def x(self):
        x = linspace(0,max(self.diffs),100)
        return x

    def fit_params(self):
        param = gamma.fit(self.diffs)
        return param

    def fit(self):
        x = self.x()
        param = self.fit_params()
        pdf_fitted = gamma.pdf(x, param[0])
        return pdf_fitted
        #return [pdf_fitted,param,x]

    def __str__(self):
        return self.name+": "+str(self.cache)

t1 = Entity("Hello")

while len(t1.cache) < 30:
    t1.mention()
    sleep(gamma.rvs(1))

print(t1.diffs)

'''
print(t1.differences())
for t in t1.differences():
    print(t)
t1fit = t1.fit()
print(t1.fit_params())

plot(t1.x(), t1fit,'-r')
hist(t1.diffs)
show()
'''
