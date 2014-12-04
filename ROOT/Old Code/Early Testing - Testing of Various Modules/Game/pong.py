from __future__ import division
from visual import *

class Paddle():
    def __init__(self): 
        self.t = 0
    def paddle(self,p_x,p_y,p_z):
        self.p = box(pos=(p_x,p_y,p_z), length=10, height=80, width=0)
    def move(self,deltat, v_x,v_y,v_z):
        current_pos = self.p.pos
        new_pos = current_pos + deltat*vector(v_x,v_y,v_z)          #(placeholder for the moment)
        self.p.pos = new_pos
        self.t = self.t + deltat
            
class Ball():
    def __init__(self): 
        self.t = 0
    def ball(self,b_x,b_y,b_z):
        self.b = box(pos=(b_x,b_y,b_z), length=10, height=10, width=0)
    def ballmove(self,deltat, bv_x,bv_y,bv_z):
        current_pos = self.b.pos
        new_pos = current_pos + deltat*vector(bv_x,bv_y,bv_z)          #(placeholder for the moment)
        self.b.pos = new_pos
        self.t = self.t + deltat
        rate(500)
        
screen = display(title='Pong', width=550, height=400,center = (250,0,0))

cursor.visible = False
screen.userzoom = False
screen.userspin = False

Player_1 = Paddle()
Player_1.paddle (0,0,0)


Player_2 = Paddle()
Player_2.paddle(500,0,0)

ball = Ball()
ball.ball(250,0,0)
m = ball.ballmove(0.1,20,20,0)


go = True
while go == True:
    if ball.b.pos[0] > 370:
        m = ball.ballmove(0.1,-1,1,0)
    ev = screen.waitfor('keydown')
    if ev.event == 'keydown':
        if ev.key == 'w':
            Player_1.move(0.1,0,90,0)
            if Player_1.p.pos[1] > 135:
                Player_1.p.pos[1] = 135
        elif ev.key == 's':
            Player_1.move(0.1,0,-90,0)
            if Player_1.p.pos[1] < -135:
                Player_1.p.pos[1] = -135
   
