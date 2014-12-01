##############################################
## A simple graph plotting script to check  ##
## if the equation I have matches the Paper ##
##############################################

import numpy as np
import pylab as plt
import math

BI_max = 720.       #Bilinear Inerpolation Max value
BI_min = 410.       #Bilinear Interpolation Min Value
Init_DR = 0.04      #Division Rate(dr) per cell per hour


def divRate(x):
    if x < 410:
        dr = Init_DR
        return dr
    if x >= 410 and x <= 715:
        dr = (BI_max - x)/(BI_max-BI_min) *(Init_DR) #Bilinear Interpolation
        return dr
    if x > 715:
        dr = 0.
        return dr

X = np.arange(0,1000,1)
V = []
for x in X:
    V.append(divRate(x))
plt.plot(X,V)
plt.axis([0,1000, -0.01, 0.05])
plt.ylabel('Division Rate per cell per hour')
plt.xlabel('Distance from Quiescent Center (um)')
plt.show()
