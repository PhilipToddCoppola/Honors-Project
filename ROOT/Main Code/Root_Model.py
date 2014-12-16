from __future__ import division
from visual import*
import math
import random as rd

##############################
##                          ##
##      Model Paramters     ##
##                          ##
##############################



vmax = 420.         #Maximum cell velocity
                    #Data derived from Beemster and Baskin 1998 paper
                    #1 python unit = 1um
a = 1./210.         #Slope of the lgositic function
b = 1100.           #Offset of the logistic function

BI_max = 720.       #Linear Inerpolation Max value
BI_min = 410.       #Linear Interpolation Min Value
Init_DR = 0.04      #Initial Division Rate taken from Beemster and Baskin 1998 paper
dt = 0.1            #Growth increment (h)
rt = 150            #Frames per second

DATA = []           #Empty List where cell sizes were inserted and checked



##############################
##                          ##
##        Cell Class        ##
##                          ##
##############################

class Cell():

    #parameters for the cell object
    def __init__(self,p_x,p_y,p_z,rad, rad2  = 5, material = materials.rough, color = color.yellow): 
        position = vector(p_x,p_y,p_z)
        self.c = ellipsoid(pos=position, axis=(0,1,0), length=rad, height=rad2, width=rad2, material = material, color = color, opacity=1)
        self.t = 0
        self.next_div = 0
        if self.divRate(self.c.pos[1])>0:
            self.next_div = (1./self.divRate(self.c.pos[1]))*(1.+0.3*(rd.random()-0.5))

    #logistic curve for cells velocity
    def velocity(self,x):
        return vmax/(1. + math.exp(-a*(x-b)))

    #check cells position and how often they should divide
    def divRate(self,x):
        if self.c.pos[1] < 410:
            dr = Init_DR
            return dr
        if self.c.pos[1] >= 410 and self.c.pos[1] <= 715:
            dr = (BI_max - x)/(BI_max-BI_min) *(Init_DR) #linear Interpolation
            return dr
        if self.c.pos[1] > 715:
            dr = 0.
            return dr

    #Cells divide based on time rather than size.
    def divide(self,deltat):
        if self.next_div>0:
            if self.t >= self.next_div:  
                old_cell_pos = self.c.pos[1]
                old_length = self.c.length
                new_cell_pos1 = old_length/4. + old_cell_pos
                new_cell_pos2 = -old_length/4. + old_cell_pos
                new_cell_length = old_length/2.
                self.c.pos[1] = new_cell_pos2 
                self.c.length = new_cell_length
                c2 = Cell(self.c.pos[0],new_cell_pos1,self.c.pos[2],new_cell_length, rad2 = 10, color = color.yellow)
                self.t=0
                return c2
            else:
                return None
        else:
            return None


    #Movement and elongation of the Cells in relation to cells above and below. 
    def elongate(self,deltat):
        Vf = self.velocity(self.c.pos[1] + (self.c.length/2.))
        Vi = self.velocity(self.c.pos[1] - (self.c.length/2.))
        Yf = (self.c.pos[1] + (self.c.length/2.)) + Vf*deltat
        Yi = (self.c.pos[1] - (self.c.length/2.)) + Vi*deltat
        self.c.length = (Yf - Yi)
        self.c.pos[1] = (Yf+Yi)/2.
        self.t = self.t + deltat


    #clear the cell object
    def clear(self):
        del self.c


###################################################################
##                                                               ##
##  Function Used to print the length of a cell to check against ##   
##  the Beemster and Baskin 1998 paper. (No longer needed)       ##                               
##                                                               ##
##    def print_length(self):                                    ##
##            DATA.append([self.c.pos[1],self.c.length])         ##
##            f = open("data.csv",'w')                           ##
##            for row in DATA:                                   ##
##                f.write(str(row[0]) + "," + str(row[1]) +"\n") ##
##            f.close()                                          ##
##                                                               ##
###################################################################



##############################
##                          ##
##      Tissue Class        ##
##                          ##
##############################

class Tissue():

    #initialises the list where cells will be saved.
    def __init__( self ):
        self.cell_list = []
        self.t = 0

    # will append new cells into the list
    def add_cell(self,cell):
        self.cell_list.append(cell)

    def grow(self,deltat,p_x,p_y,p_z, v_x,v_y,v_z,color):

        # New cells are initiated
        if int(self.t/deltat) % 42 == 0:
            R = [rd.random(),rd.random(),rd.random(),rd.random()]
            for c in range(3):
                r = (R[c]-0.5)*0.2
                cell = Cell(p_x,p_y-10.*r*0.5,p_z,10.*(1.+r),10.,materials.rough, color)
                self.add_cell(cell)
                p_x = p_x+10

        # Existing cells are moving
        for i in range(len(self.cell_list)-1, -1, -1):              
            cell = self.cell_list[i]                                

            #Call the movement and elongation methods
            cell.elongate(deltat) 
            for i in range(len(self.cell_list)-1, -1, -1):
                cell = self.cell_list[i] 

                # cell division
                c2 = cell.divide(deltat)
                if c2 != None:
                    self.add_cell(c2)

                # Remove cells that reach the boundaries
                if cell.c.pos[1] > 2000 - cell.c.length/2:                                    
                    cell.clear()
                    del cell                                            
                    del self.cell_list[i]
                    
        # update time
        self.t = self.t + deltat



##############################
##                          ##
##    Main Program Loop     ##
##                          ##
##############################          

#create the environment
screen = display(title='Root Development Model', width=640, height=940, autoscale = False, center = (0,100,0))
root_shadow = cylinder(pos=(0,-100,0), axis=(0,2100,0),radius=75, material=materials.rough, color=color.green, opacity=0.4)
meri_scale = curve(pos=[(100,0,0),(100,300,0)],color = color.blue)
elong_scale = curve(pos=[(100,300,0),(100,750,0)], color = color.red)


#program runs
root = Tissue()
for i in range(10000):
    #calls the grow method
    root.grow(dt,-10,0,0,0,0.1,0,color.yellow)
    rate(rt)

    #simple camera manipulation
    if screen.mouse.clicked:
        m = screen.mouse.getclick()
        screen.center[1] += 100
        if screen.center[1] > 2000:
            screen.center[1] = 100
