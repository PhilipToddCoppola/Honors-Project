##############################################
## A simple graph plotting script to check  ##
## if the equation I have matches the Paper ##
##############################################

import numpy as np
import pylab as plt
import math

vmax = 420.     
a = 1./210.
b = 1100  

def velocity(x):
    return vmax/(1. + math.exp(-a*(x-b)))

X = np.arange(-1000,3001,100)
V = []
for x in X:
    V.append(velocity(x))
plt.plot(X,V)
plt.axis([-500,3000,0,450])
plt.ylabel('Velocity (um per Hour)')
plt.xlabel('Distance from Quiescent Center (um)')
plt.show()
