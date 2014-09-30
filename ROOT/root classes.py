from visual import *
import random

class Cells():
    def pos(self, p_x, p_y, p_z):
        position = (p_x,p_y,p_z)
        
    def cell(self, position, rad, color):
        sphere(pos = position ,radius = rad, color = color)

    def velocity (self,vector,x,y,z):
        self.vector = vector(x,y,z)
    
screen = display(title='Root Development Model', width=640, height=720,center=(0,-3,0))

meristem = Cells()
x = 0
r = 3

meristem.pos (0,0,0)
meristem.cell(meristem.pos, r,color.green)

meristem.velocity(vector, 0.3,0,0)

deltat =0.005
t=0

while t <10:
    meristem.pos = meristem.pos + (meristem.velocity*deltat)

    rate(50)

'''
for m in range(50):
    meristem.cell(x,0,0,r,color.green)
    x+=0.3
''' 


        
        
