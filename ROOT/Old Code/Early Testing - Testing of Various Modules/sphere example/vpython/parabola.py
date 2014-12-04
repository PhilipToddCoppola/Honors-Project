from visual import*


line = curve(x=arange(0,7.2,0.1), radius= 3)
line.color= color.green
line.radius = .3
line.y = (6/4.5) * ((line.x - 2)**2) -10
line2 = curve(x=arange(-7.1,0.1,0.1), radius= 3)
line2.color= color.green
line2.radius = .3
line2.y = (6/4.5) * ((line2.x + 2)**2) -10

ring = ring(pos=(0,-7,0), axis=(0,1,0), radius=2.5, thickness=0.5)
ring.color = color.red

root_shadow = cone(pos=(0,25,0), axis=(0,-50,0),radius=10, color=color.green, opacity=0.4)
meristem = sphere(pos = (0,-5,0),radius = 1.5, color=color.yellow)
meristem2= sphere(pos = (0,-5,0),radius = 1.5, color=color.yellow)
meristem3= sphere(pos = (0,-5,0),radius = 1.5, color=color.yellow)
#add deltat and shiz to follow the lines for the meristem
meristem2.velocity = (6/4.5) * ((line.x - 2)**2) -10
meristem3.velocity = (6/4.5) * ((line2.x + 2)**2) -10
deltat=0.005
t=0
while t < 10:
    meristem2.pos = meristem2.pos + (meristem2.velocity*deltat)
    meristem3.pos = meristem3.pos + (meristem3.velocity*deltat)
    t=t+deltat
    rate(100)
