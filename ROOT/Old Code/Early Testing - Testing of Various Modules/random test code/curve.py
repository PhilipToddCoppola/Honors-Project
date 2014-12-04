from visual import*

def R(x):
    y = -(1.0/4.0)*x**2 + 4
    return y

dx = 0.5

a = 0.0

b = 3.0

x_axis = curve(pos=[(-10,0,0),(10,0,0)])

y_axis = curve(pos=[(0,-10,0),(0,10,0)])

z_axis = curve(pos=[(0,0,-10),(0,0,10)])

line = curve(x=arange(0,3,.1))
line.color=color.cyan
line.radius = .1
line.y = -(1.0/4.0) * (line.x**2) + 4

#scene.background = color.white

for i in range(-10, 11):

    curve(pos=[(-0.5,i),(0.5,i)])
    curve(pos=[(i,-0.5),(i,0.5)])

VT = 0


for x in arange(a + dx,b + dx,dx):

    V = pi * R(x)**2 * dx

    disk = cylinder(pos=(x,0,0),radius=R(x),axis=(-dx,0,0), color = color.yellow)

    VT = V + VT

    print V

print "Volume =", VT
