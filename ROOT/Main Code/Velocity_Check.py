##############################################
## A simple graph plotting script to check  ##
## if the equation I have matches the Paper ##
##############################################

import numpy as np
import pylab as plt
import math

vmax = 400.     
a = 1./125./2
b = 1100  

def velocity(x):
    return vmax/(1. + math.exp(-a*(x-b)))

X = np.arange(-1000,3000,1)
V = []
for x in X:
    V.append(velocity(x))
plt.plot(X,V)
plt.show()
