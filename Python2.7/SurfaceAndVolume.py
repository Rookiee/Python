#import math
from math import *
def SurAndVol(r):
	if(r >= 0):
		print "Area is %s " %(4*pi*r**2)
		print "Volume is %s " %((3.0/4) * pi * r**3)
	else:
		print "ERROR"

r = input ("Input the radius of a sphere: ")
SurAndVol(r)


