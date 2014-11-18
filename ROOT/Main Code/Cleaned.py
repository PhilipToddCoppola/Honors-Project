from __future__ import division
from visual import*
import math



# Model paramters
vmax = 420.     # maximum cell velocity
                # data derived from Beemster and baskin 1998
                # 1 python unit = 1um
a = 1./210      # slope of the lgositic function
b = 1100        # offset of the logistic function



#Create Cell Class
class Cell():

    #parameters for the cell object
    def __init__(self,p_x,p_y,p_z,rad, rad2  = 5, material = materials.rough, color = color.yellow): 
        position = vector(p_x,p_y,p_z)
        self.c = ellipsoid(pos=position, axis=(0,1,0), length=rad, height=rad2, width=rad2, material = material, color = color, opacity=1)
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

    #cells divide
    def divide(self,deltat):
        if self.c.pos[1] < 400 :
            if self.c.length > 15: #will standardise the time each cell divides
                old_cell_pos = self.c.pos[1]
                new_cell_pos = ((self.c.length/2)/2) + old_cell_pos
                old_cell_pos = (-(self.c.length/2)/2) + old_cell_pos
                new_cell_length = (self.c.length/2)                
                self.c.pos[1] = old_cell_pos
                self.c.length = new_cell_length
                c2 = Cell(self.c.pos[0],new_cell_pos,self.c.pos[2],new_cell_length, rad2 = 10, color = color.red)
                return c2
            else:
                return None
        else:
            return None

    #grow the cells while touching the cells above and below it
    def elongate(self,deltat):
        Vf = self.velocity(self.c.pos[1] + (self.c.length/2)) #elongation stoppes after vmax on logistic curve. Need to keep it going.
        Vi = self.velocity(self.c.pos[1] - (self.c.length/2))
        Yf = (self.c.pos[1] + (self.c.length/2)) + Vf*deltat
        Yi = (self.c.pos[1] - (self.c.length/2)) + Vi*deltat
        self.c.length = (Yf - Yi)
        self.c.pos[1] = (Yf+Yi)/2
        if self.c.length > 75:
            self.c.length == 75

    #clear the cell object
    def clear(self):
        del self.c
            


#Create Tissue Class
class Tissue():

    #initialises the list where cells will be saved.
    def __init__( self ):
        self.cell_list = []
        self.t = 0

    # will append new cells into the list
    def add_cell(self,cell):
        self.cell_list.append(cell)

    def grow(self,deltat,p_x,p_y,p_z, v_x,v_y,v_z,color):

        # New cells are being initiated
        if int(self.t/deltat) % 17 == 0:                            
            cell = Cell(p_x,p_y,p_z,10.,10,materials.rough, color)
            self.add_cell(cell)

        # Existing cells are moving
        for i in range(len(self.cell_list)-1, -1, -1):              
            cell = self.cell_list[i]                                
            cell.move(deltat,v_x,v_y,v_z)
            c2 = cell.divide(deltat)
            if c2 != None:
                self.add_cell(c2)
            cell.elongate(deltat)
            if cell.c.pos[1] > 2000 - cell.c.length/2:                                    
                cell.clear()
                del cell                                            
                del self.cell_list[i]                               

        # update time
        self.t = self.t + deltat

           

#create the environment
screen = display(title='Root Development Model', width=640, height=940,
                 autoscale = False, center = (0,100,0))
root_shadow = cylinder(pos=(0,-100,0), axis=(0,2100,0),radius=75, material=materials.rough, color=color.green, opacity=0.4)
meri_scale = curve(pos=[(100,0,0),(100,300,0)],color = color.blue) # 300 um meristem zone marker
elong_scale = curve(pos=[(100,300,0),(100,750,0)], color = color.red) # 450um elongation zone marker
test_cell = ellipsoid(pos=(20,900,0), axis=(0,1,0), length=75, height=10, width=10, material = materials.rough, color = color.red, opacity=1)
label = label(pos = test_cell.pos, text ='Cell Size Check of 75um', xoffset = 50,yoffset = 10, space=test_cell.width, border = 6, font='sans')



#program runs
root = Tissue()
for i in range(10000):
    root.grow(0.2,0,0,0,0,0.1,0,color.yellow)
    rate(30)
    if screen.mouse.clicked:
        m = screen.mouse.getclick()
        screen.center[1] += 100
        if screen.center[1] > 2000:
            screen.center[1] = 100
