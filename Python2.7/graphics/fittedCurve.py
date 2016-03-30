from matplotlib import *
from numpy import *
from scipy import *
from scipy.optimize import leastsq

def fun2(p,x):
	f = poly1d(p)
	return f(x)

def err(p,x,y):
	return y - fun2(p,x)

xmin = 0
xmax = 10

x = linspace(xmin,xmax,15)
x1 = linspace(xmin,xmax,1000)
y1 = x + random.randn(len(x))

p0 = random.randn(10)

result = leastsq(err,p0,args = (x,y1),maxfev=1000)

print "agrument: ",result[0]
title("least - squares fited curve to discrete data")
plot(x,y1,'ro',label = 'data')
plot(x1,fun2(result[0],x1), label = 'Fitted curve ')

legend()

show()
