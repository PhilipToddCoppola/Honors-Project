from __future__ import division
from visual import*
import math

# Model paramters
vmax = 400.     # maximum cell velocity
                # data derived from Beemster and baskin
                #1 python unit = 2um
a = 1./150./2    # slope of the lgositic function
b = 550         # offset of the logistic function
#Create Cell Class
class Cell():
    #parameters for the cell object
    def __init__(self,p_x,p_y,p_z,rad, material, color): 
        position = vector(p_x,p_y,p_z)
        self.c = ellipsoid(pos=position, axis=(0,1,0), length=rad, height=rad, width=rad, material = material, color = color, opacity=1)
        self.t = 0
    #logistic curve for cells velocity
    def velocity(self,x):
        return vmax/(1. + math.exp(-a*(x-b)))
    #Cell movement upwards
    def move(self,deltat,v_x,v_y,v_z):
        current_pos = self.c.pos
        new_pos = current_pos + deltat*self.velocity(self.c.pos[1])*vector(v_x,v_y,v_z)
        self.c.pos = new_pos
        self.t = self.t + deltat
    def elongate(self,deltat):
        Vf = self.velocity(self.c.pos[1] + (self.c.length/2)) #elongation stoppes after vmax on logistic curve. Need to keep it going.
        Vi = self.velocity(self.c.pos[1] - (self.c.length/2))
        Yf = (self.c.pos[1] + (self.c.length/2)) + Vf*deltat
        Yi = (self.c.pos[1] - (self.c.length/2)) + Vi*deltat
        self.c.length = (Yf - Yi)
        self.c.pos[1] = (Yf+Yi)/2           

    def divide(self, deltat):
        pass  
    #clear the cell object
    def clear(self):
        del self.c

#Create Tissue Class
class Tissue():
    #initialises the list where cells will be saved.
    def __init__( self ):
        self.cell_list = []
        self.t = 0
##        self.num=0
    # will append new cells into the list
    def add_cell(self,cell):
        self.cell_list.append(cell)
    def grow(self,deltat,p_x,p_y,p_z, v_x,v_y,v_z,color):
        # New cells are being initiated
        if int(self.t/deltat) % 7 == 0:                            
            cell = Cell(p_x,p_y,p_z,5.,materials.rough, color)   
            self.add_cell(cell)
##            print (self.cell_list)
##            self.num += 1
##            print(self.num)
        # Existing cells are moving
        for i in range(len(self.cell_list)-1, -1, -1):              
            cell = self.cell_list[i]                                
            cell.move(deltat,v_x,v_y,v_z)
            cell.elongate(deltat)
            #delete information of the cell
            if cell.c.pos[1] > 2000 - cell.c.length/2:                                    
                cell.clear()
                del cell                                            
                del self.cell_list[i]                               
        # update time
        self.t = self.t + deltat
    def markers(self, deltat,m_y):
            marker = box(pos=(70,m_y,0), length = 5, width = 5, height = 1, color = color.orange, material = materials.rough)
            
