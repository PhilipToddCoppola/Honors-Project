from visual import *

class sin_func:
    def __init__(self, x, amp=1., freq=1., phase=0.0):
        self.x = x
        self.amp = amp
        self.freq = freq
        self.phase = phase

        self.curve = curve(color=color.red, x=self.x, y=self.f(x), radius=0.05)
        self.label = label(pos=(xmin/2.0,ymin), text="Hi",box=False, height=30)
        
    def f(self, x):
        y = self.amp * sin(self.freq*x+self.phase)
        return y

    def update(self, amp, freq, phase):
        self.amp = amp
        self.freq = freq
        self.phase = phase
        self.curve.y = self.f(x)
        self.label.text = self.get_eqn()

    def get_eqn(self):
        if self.phase == 0.0:
            tphase = ""
        elif (self.phase > 0):
            tphase = u" + %i\u03C0/8" % int(self.phase*8.0/pi)
        else:
            tphase = u" - %i\u03C0/8" % int(abs(self.phase*8.0/pi))
        print self.phase*8.0/pi

        txt = "y = %ssin(%sx %s)" % (simplify_num(self.amp), simplify_num(self.freq), tphase)
        return txt
    
def simplify_num(num):
    if (num == 1):
        snum = ""
    elif (num == -1):
        snum = "-"
    else:
        snum = str(num).split(".")[0]+" "
    return snum
        
amp = 1.0
freq = 1.0

damp = 1.0
dfreq = 1.0

phase = 0.0
dphase = pi/8.0

xmin = -2*pi
xmax = 2*pi
dx = 0.1

ymin = -3
ymax = 3

scene.width=640
scene.height=480

xaxis = curve(pos=[(xmin,0),(xmax,0)])
yaxis = curve(pos=[(0,ymin),(0,ymax)])

x = arange(xmin, xmax, dx)
#y = f(x)

func = sin_func(x=x)
func.update(amp, freq, phase)

while 1: #theta <= 2*pi:
    rate(60)

    if scene.kb.keys: # is there an event waiting to be processed?
        s = scene.kb.getkey() # obtain keyboard information
        #print s
        if s == "up":
            amp += damp
        if s == "down":
            amp -= damp
        if s == "right":
            freq += dfreq
        if s == "left":
            freq -= dfreq

        if s == "s":
            phase += dphase
        if s == "a":
            phase -= dphase

        func.update(amp, freq, phase)
        #update_curve(func, y)
        
