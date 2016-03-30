from random import random
from math import sqrt
from time import clock
Darks = 999999999999l
hits = 0.0
clock()
for i in range(1,Darks):
	x,y = random(), random()
	dist = sqrt(x**2 + y**2)
	if dist <= 1.0:
		hits = hits + 1
pi = 4 * (hits/Darks)
print "pi is %s" %(pi)
print "running time is % -5.5ss" %clock()

