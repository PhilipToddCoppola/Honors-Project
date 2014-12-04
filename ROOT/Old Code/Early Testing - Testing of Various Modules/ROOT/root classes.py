from visual import *
import random

class Cells():

    def cell(self, p_x, p_y, p_z, rad, color):
        sphere(pos = vector(p_x,p_y,p_z) ,radius = rad, color = color)

screen = display(title='Root Development Model', width=640, height=720,center=(0,-3,0))

meristem = Cells()
p_x = 0
p_y = 0
p_z = 0
r = 3

#meristem.pos (0,0,0)
meristem.cell(p_x,p_y,p_z, r,color.green)

#meristem.velocity(vector, 0.3,0,0)

deltat =0.005
t=0

for m in range(50):
    meristem.cell(p_x,p_y,p_z,r,color.green)
    p_x+=0.3


        
        
'''
    def pos(self, p_x, p_y, p_z):
        position = (p_x,p_y,p_z)

   def velocity (self,vector,x,y,z):
       self.vector = vector(x,y,z)

while t <10:
    meristem.pos = meristem.pos + (meristem.velocity*deltat)

    rate(50)
'''
