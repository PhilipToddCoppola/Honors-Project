from visual import *

class spaceship1:

    def __init__(self):

        self.f = frame()
        self.r = ring(frame=self.f, thickness=.25, axis=(0,1,0))
        self.cabin = sphere(frame=self.f, radius=0.6, color=color.red)
        self.front = pyramid(frame=self.f, height=1,width=1,length=2, color=color.blue)
        self.trail = curve(pos=[self.f.pos,])

    def turn_xz(self, turn_rate):
        self.f.axis = rotate(self.f.axis, turn_rate, (0,1,0))

    def move_xz(self, speed):
        self.f.pos = self.f.pos + self.f.axis*speed
        self.trail.append(pos=self.f.pos)
                          

class missile:
    def __init__(self, axis, pos):

        self.f = frame(axis=axis, pos=pos)
        self.r = sphere(frame=self.f, radius=0.2, color=color.green)
        self.speed = 0.5
        

    def move_xz(self):
        self.f.pos = self.f.pos + self.f.axis*self.speed

class bounds:
    def __init__(self, boundary_distance):
        self.boundary_distance = boundary_distance
        self.border = curve(pos=[(-boundary_distance,0,-boundary_distance),
                                 (boundary_distance,0,-boundary_distance),
                                 (boundary_distance,0,boundary_distance),
                                 (-boundary_distance,0,boundary_distance),
                                 (-boundary_distance,0,-boundary_distance)])
    def in_bounds(self, pos):
        if ( pos.x < -self.boundary_distance or
             pos.x > self.boundary_distance or
             pos.z < -self.boundary_distance or
             pos.z > self.boundary_distance):
            return false
        else:
            return true
        

ss = spaceship1()
turn = 0.0
speed=0.0
l_track_ship = 1
scene.range=10
scene.forward = (0,-1,0)
missiles = []

boundary_distance = 100
boundary = bounds(boundary_distance)

while 1:
    rate(20)

    if l_track_ship > 0:
        scene.center = ss.f.pos
    
    ss.turn_xz(turn)
    ss.move_xz(speed)

    #move missiles
    del_list = []
    for i, m in enumerate(missiles):
        m.move_xz()

        #delete missile if out of bounds
        if boundary.in_bounds(m.f.pos) == False:
            del_list.append(i)
    for i in del_list:
        missiles[i].f.visible = False
        del missiles[i]
            
    
    #if m <> None:
    #    m.move_xz()

    if scene.kb.keys: # event waiting to be processed?
        s = scene.kb.getkey() # get keyboard info

        if s == 'left':
            turn = turn + 0.01
        if s == 'right':
            turn = turn - 0.01

        if s == 'up':
            speed = speed + 0.01
        if s == 'down':
            speed = speed - 0.01

        if s == ' ':
            if turn <> 0:
                turn = 0
            elif speed <> 0:
                speed = 0

        #fire missile
        if s == 'a':
            missiles.append(missile(ss.f.axis, ss.f.pos))
