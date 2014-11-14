
from classes import*

#create the environment
screen = display(title='Root Development Model', width=640, height=940,
                 autoscale = False, center = (0,100,0))
root_shadow = cylinder(pos=(0,-100,0), axis=(0,2100,0),radius=37.5, material=materials.rough, color=color.green, opacity=0.4)
meri_scale = curve(pos=[(75,0,0),(75,300,0)],color = color.blue) # 300 um meristem zone marker
elong_scale = curve(pos=[(75,300,0),(75,750,0)], color = color.red) # 450um elongation zone marker

root = Tissue()

#Main Program Loop
for i in range(10000):
    root.grow(0.005,0,0,0,0,0.1,0,color.yellow)
    root.grow(0.005,4,0,0,0,0.1,0,color.yellow)
    
    rate(30)
    if screen.mouse.clicked:
        m = screen.mouse.getclick()
        screen.center[1] += 100
        if screen.center[1] > 2000:
            screen.center[1] = 100
