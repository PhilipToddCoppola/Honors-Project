from visual import *

ball=sphere(pos=vector(-5,0,0),radius=1,color=color.cyan)
wallR = box(pos=(6,0,0), size=(0.2,12,12), color=color.green)
wallL = box(pos=(-8,0,0), size=(0.2,12,12),color=color.green)
wallT = box(pos=(-1,6,0), size=(14,0.2,12), color=color.blue)
wallBo= box(pos=(-1,-6,0), size=(14,0.2,12), color=color.blue)
wallBa= box(pos=(-1,0,-6), size=(14,12,0.2), color=color.red)
wallF = box(pos=(-1,0,6), size=(14,12,0.2), color=color.red, opacity=0)

ball.velocity = vector(25,5,15)
vscale=0.1
varr = arrow(pos=ball.pos,axis=vscale*ball.velocity,color=color.yellow)
deltat = 0.005
t = 0
ball.trail = curve(color=ball.color)
scene.autoscale = False
while t < 10:
    if ball.pos.x > wallR.pos.x:
        ball.velocity.x = -ball.velocity.x
        varr.axis.x = -varr.axis.x

    if ball.pos.x < wallL.pos.x:
        ball.velocity.x = -ball.velocity.x
        varr.axis.x = -varr.axis.x

    if ball.pos.y > wallT.pos.y:
        ball.velocity.y = -ball.velocity.y
        varr.axis.y = -varr.axis.y

    if ball.pos.y < wallBo.pos.y:
        ball.velocity.y = -ball.velocity.y
        varr.axis.y = -varr.axis.y

    if ball.pos.z < wallBa.pos.z:
        ball.velocity.z = -ball.velocity.z
        varr.axis.z = -varr.axis.z

    if ball.pos.z > wallF.pos.z:
        ball.velocity.z = -ball.velocity.z
        varr.axis.z = -varr.axis.z        

        
    ball.pos = ball.pos + (ball.velocity*deltat)
    varr.pos = ball.pos + ball.velocity*deltat
    ball.trail.append(pos=ball.pos)
    t = t + deltat
    rate(100)
