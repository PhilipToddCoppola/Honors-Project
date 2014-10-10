


from __future__ import division
from visual import *

class Cell():                                  
    def __init__(self,p_x,p_y,p_z, rad, material, color): 
        position = vector(p_x,p_y,p_z)
        #self.c = sphere(pos=position, radius = rad, material = material, color=color)
        self.c = ellipsoid(pos=position, axis=(0,1,0), length=3*rad, height=rad, width=rad, material = material, color = color)
        self.t = 0
    def move(self,deltat, v_x,v_y,v_z):
        current_pos = self.c.pos
        new_pos = current_pos + deltat*vector(v_x,v_y,v_z)          #(placeholder for the moment)
        #new_pos = current_pos + deltat*velocity*vector(v_x,v_y,v_z) replace veolcity with data from the paper  http://www.plantphysiol.org/content/116/4/1515
        self.c.pos = new_pos
        self.t = self.t + deltat
    def clear(self):
        del self.c


class Tissue():
    #initialises the list where cells will be saved.
    def __init__( self ):
        self.cell_list = []
        self.t = 0
    # will append new cells into the list
    def add_cell(self,cell):
        self.cell_list.append(cell)
    def grow(self,deltat, v_x,v_y,v_z,v_x2,v_y2,v_z2,v_x3,v_y3,v_z3):
        # New cells are being initiated
        if int(self.t/deltat) % 28 == 0:                            #creates a cell when the remainder of the calculation in points of 20 is 0
            cell = Cell(0,-5,0,1.5,materials.rough, color.yellow)   #creates the cell
            root.add_cell(cell)                                     #calls the add_cell method and places the new cells into the list

        # Existing cells are moving
        for i in range(len(self.cell_list)-1, -1, -1):              # moves down the length of the list where the cells info is stored
            cell = self.cell_list[i]                                # saves it into a variable called cell
            cell.move(deltat,v_x,v_y,v_z)                           # calls the .move method to update the position of the cells (i.e moving upward
            if cell.c.pos[1]>23:                                    # when the y position reaches a specified value...
                cell.clear()                                        # ...call the clear method which deletes the physical sphere...
                del cell                                            # ...the cell object ...
                del self.cell_list[i]                               # ...and the data in the list
            
        # update time
        self.t = self.t + deltat
        

screen = display(title='Root Development Model', width=640, height=720, autoscale = False, center = (0,7,0))
root_shadow = cone(pos=(0,25,0), axis=(0,-50,0),radius=10, material=materials.rough, color=color.green, opacity=0.4)

  
root = Tissue()

for i in range(10000):
    root.grow(0.1,0,1,0,-16,1,0,16,1,0)
    rate(75)
'''   
Go = True                           #CONTINUOUS RUNNING (slightly more cpu usage)
while Go == True:
    root.grow(0.1,0,1,0)
    rate(75)
'''

'''
implementation of cell elongation. Possible routes:

1 - add in multiple cells at one location to elongate later
2 - create cells when it is time for the current cell to elongate

Current thinking:Option 2 is the best route as this takes away the issue of memory
problems down the line.

How to implement???
in the grow method, an if statement checks if the cell is at a certain location.
It will add two further cells which will move left and right respective of the cell

if cell.c.pos[1] > 5: #will be used to elongate
    cell_x = Cell(0,5,0,1.5,materials.rough, color.yellow)          this code is planned to create a cell when a cell hits y = 5
    cell_y = Cell(0,5,0,1.5,materials.rough, color.yellow)          constantly creates cells like crazy. (==) does nothing (?)
    cell_x.move(deltat,-1,1,0)
    cell_y.move(deltat,1,1,0)


if int(self.t/deltat) % 28 == 0:
    cell2 = Cell(0,5,0,1.5,materials.rough, color.yellow)           This like in the grow method creates one every tick...
    root.add_cell(cell)                                             right from the start... not good.
                                                                    Both have flaws...find a way to combine?



if cell.c.pos[1] == 7:
    if int(self.t/deltat) % 28 == 0:
    cell2 = Cell(0,5,0,1.5,materials.rough, color.yellow)
    root.add_cell(cell2)

                                                                    like so?
                                                                    

if cell.c.pos[1] == 7:
    if int(self.t/deltat) % 28 == 0:
        cell2 = Cell(0,5,0,1.5,materials.rough, color.yellow)
        root.add_cell(cell2)


                                                                    possible use of ellipsoids rather than spheres???
'''



