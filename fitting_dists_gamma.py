from scipy.stats import norm,gamma
from numpy import linspace
from pylab import plot,show,hist,figure,title

a = 5
samp = gamma.rvs(a,loc=3,scale=3,size=200)
param = gamma.fit(samp)
print(param)

x = linspace(0,60,100)
pdf = gamma.pdf(x,a,loc=3,scale=3)
pdf_fitted = gamma.pdf(x,param[0],loc=param[1],scale=param[2])

title('Gamma Distrubution')
plot(x,pdf_fitted,'r-',x,pdf,'b-')
hist(samp,normed=1,alpha=.3)
show()
