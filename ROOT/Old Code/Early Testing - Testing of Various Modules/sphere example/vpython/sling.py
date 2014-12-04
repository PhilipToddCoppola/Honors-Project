from visual import *    

class pull_cord:

    def __init__(self, p0, p1):
        self.ball = sphere(material=materials.wood, pos=p1)
        self.cord = curve(pos=[p0,p1], radius=0.2,
                          color = color.blue)
        self.ballstart = self.ball.y
        self.maxlength = 15.0
        self.initial_p0 = p0
        self.initial_p1 = p1

    def reset(self):
        p0 = self.initial_p0
        p1 = self.initial_p1
        self.ball.pos = p1
        self.cord.pos = [p0,p1]
        self.ballstart = self.ball.y
        initial_p0 = p0
        initial_p1 = p1
        


scene.range = 25
scene.ambient = color.gray(0.5)

# reset button
reset = sphere(pos=(-20,-22), color=color.blue, material=materials.plastic)

# release button
release = sphere(pos=(-2,-22), color=color.blue, material=materials.plastic)

# show vector button
show_vector = sphere(pos=(-13,-22), color=color.blue, material=materials.plastic)


# show Forces button
show_forces = sphere(pos=(-16,-22), color=color.blue, material=materials.plastic)

# Create a ball
ball = sphere(pos=(20.5,-20), material = materials.marble, color=(1,0.7,0.7))
ball.initial_pos = ball.pos * 1.0
ball.move = False

# create velocity vector
speed = 5
v = arrow(pos=ball.pos, axis=(0,speed,0), shaftwidth=0.2, headwidth=0.6)
v.initial_axis = v.axis * 1.0

# Create Force vectors
Fcp = arrow(pos=ball.pos, axis=(0,0,0), shaftwidth=0.4, headwidth=1.0,
            color=color.yellow)
Fcp.scale = 2.0


# Create string to catch the ball
string = curve(pos=[(0,0),(20,0)], radius=0.2,
               color=color.blue)
string.initial_p1 = string.pos[1] * 1.0
string.spin = False
hit_check = True
string.r = string.pos[1][0] - string.pos[0][0]  #radius
string.circ = 2 * pi * string.r                 #circumference

# Create pull cord
pull = pull_cord(vector(0,0,0), vector(0,-5,0))


# Create target
target = sphere(pos=(0, 300), radius = 30, up=(0,0,1),
                material=materials.BlueMarble)

# Create the spring launcher
spring = helix(pos=(20.5, -24,0), axis=(0,4,0), coils=5, radius=0.5, thickness=0.2,
               color=color.red)

# Instructions
show_instructions = True
v_instr = label(text="Adjust arrow \nto set speed",
                pos=v.pos+v.axis, xoffset=-70, yoffset=30,
                height=10, space=5)

fire_instr = label(text="Click ball \nto launch",
                   pos=ball.pos, xoffset=-70, yoffset=10,
                   height=10, space=10)


dt = 0.05

by = 0.75 # click this close to tail or tip
drag = None # have not selected tail or tip of arrow
pick = None

while 1:


    rate(4/dt)

    # move ball
    #if spin the string
    if ball.move:
        if string.spin:
            oldpos = ball.pos * 1.0
            string.pos[1] = ball.pos.rotate(speed*dt*2*pi/string.circ, vector(0,0,1))
            ball.pos =  string.pos[1]
            #print speed
            vec  = (ball.pos - oldpos)/dt
            vx = vec.x
            vy = vec.y
            # Centripetal force
            Fcp.pos = ball.pos
            Fcp.mag = mag(v.axis) * mag(v.axis) / mag(string.pos[1])
            Fcp.axis = -norm(string.pos[1])*Fcp.mag*Fcp.scale
        else:
            ball.pos.x += vx*dt
            ball.pos.y += vy*dt

        v.pos = ball.pos
        v.axis.x = vx
        v.axis.y = vy
        v.axis = norm(v.axis)*speed
        #print "m", mag(v.axis)


    # rotate when the ball hits the string
    if hit_check and ball.pos.y >= 0: # hit
        ball.pos.y = 0.0
        string.spin = True
        hit_check = False
        initial_momentum = speed * mag(string.pos[1] - string.pos[0])
        print initial_momentum
        #print "hit"

    # hit the target
    if mag(ball.pos-target.pos) <= ball.radius+target.radius:
        target.color = color.red


    # mouse interactions
    if scene.mouse.events:
        m1 = scene.mouse.getevent() # obtain event
        if m1.press:
            if mag(v.pos-m1.pos) <= by:
                drag = 'tail' # near tail of arrow
            elif mag((v.pos+v.axis)-m1.pos) <= by:
                drag = 'tip' # near tip of arrow
            drag_pos = m1.pos # save press location
        elif m1.drag and m1.pick == pull.ball and string.spin:
            drag_pos = m1.pickpos
            pick  = m1.pick
            scene.cursor.visible = 0
            
        elif m1.drop: # released at end of drag
            drag = None # end dragging (None is False)
            scene.cursor.visible = 1
            pick = None

        # FIRE ball
        if m1.pick == ball and m1.release:
            ball.color = color.red
            ball.move = True
            vx = v.axis.x
            vy = v.axis.y
            speed = mag(v.axis)
            show_instructions = False
            v_instr.visible = 0
            fire_instr.visible = 0
            #initial_speed = speed

        # RELEASE
        if m1.pick == release and m1.release:
            string.spin = False
            Fcp.axis = vector(0,0,0)
            

        # SHOW VECTOR
        if m1.pick == show_vector and m1.release:
            if v.visible == 0:
                v.visible = 1
            else:
                v.visible = 0

        # SHOW Forces
        if m1.pick == show_forces and m1.release:
            if Fcp.visible == 0:
                Fcp.visible = 1
            else:
                Fcp.visible = 0

        # RESET
        if m1.pick == reset:
            string.spin = False
            hit_check = True
            pull.reset()
            string.pos[1] = string.initial_p1
            ball.pos = ball.initial_pos
            print ball.pos, ball.initial_pos
            ball.move = False
            v.axis = v.initial_axis
            v.pos = ball.pos
            speed = mag(v.axis)
            target.color = color.white
    
    # move pull cord
    if pick:
        new_pos = scene.mouse.project(normal=(0,0,1))
        if new_pos != drag_pos:

            if (pick == pull.ball and
                new_pos.y < pull.ballstart and
                new_pos.y > pull.ballstart - pull.maxlength and
                string.spin):

                dy = new_pos.y - drag_pos.y
                pick.pos.y += new_pos.y - drag_pos.y
                drag_pos = new_pos
                pull.cord.pos[1] = pull.ball.pos

                # adjust the string length
                oldlength = mag(string.pos[0]-string.pos[1])
                newlength = mag(string.pos[0]-string.pos[1]) + dy
                string.pos[1] = string.pos[1] * newlength/oldlength
                ball.pos =  string.pos[1]

                #conserve momentum
                speed = speed * oldlength / newlength

                #print newlength, speed
                
        
            

            
    if drag:
        new_pos = scene.mouse.pos
        if new_pos != drag_pos: # if mouse has moved
            displace = new_pos - drag_pos # moved how far
            drag_pos = new_pos # update drag position
            if drag == 'tip':
                # only allow movement in y direction
                v.axis.y += displace.y # displace the tip
