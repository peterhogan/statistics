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

    def ld(self,inputfile):
        with open(inputfile, 'r') as f:
            fileopen = f.read()
            lines = fileopen.splitlines()
            quoteless = [i[1:-1] for i in lines]
        self.cache = quoteless
        self.differences()

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
    def trim(self, amount):
        perc = int(amount * len(self.diffs))
        self.diffs = sorted(self.diffs)[:-perc]

    def x(self):
        x = linspace(0,max(self.diffs),len(self.diffs))
        return x

    def fit_params(self):
        param = gamma.fit(self.diffs)
        return param

    def fit(self):
        x = self.x()
        param = self.fit_params()
        pdf_fitted = gamma.pdf(x, param[0], param[1], param[2])
        return pdf_fitted
        #return [pdf_fitted,param,x]

    def __str__(self):
        return self.name+": "+str(self.cache)

'''
loc_pars = []
for i in linspace(0.05,0.4,100):
    t2 = Entity(str(i))
    t2.ld('all.list')
    print('Cleaning by',i,'..')
    t2.clean(i)
    t2fit = t2.fit()
    fitp = t2.fit_params()
    print(fitp)
    loc_pars.append(fitp[1])

print(loc_pars)
print(min([abs(i) for i in loc_pars]))
'''

avls = []

t2 = Entity('test')
t2.ld('noall.list')
x = t2.x()

a_val = 0
incr = 0.01
val = 0.27
#while a_val < 1:
while len(avls) < 60:
    t2 = Entity('test')
    t2.ld('noall.list')
    t2.trim(val)
    t2fit = t2.fit()
    fps = t2.fit_params()
    a_val = fps[0]
    avls.append(a_val)
    print("Trimming",val," -- at --",a_val)
    val += incr
    plot(t2.x(), t2fit)

#plot(range(len(avls)),avls)

#plot(t2.x(), t2fit,'-r')
hist(t2.diffs,normed=1,alpha=0.3)
show()
