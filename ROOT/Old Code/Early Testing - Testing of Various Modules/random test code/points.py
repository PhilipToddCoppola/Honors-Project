from visual import *
import random

n = 0
while n <= 2500:
    r_x = random.randrange(-100, 100)
    r_y = random.randrange(-100, 100)
    r_z = random.randrange(-100, 100)
    points(pos=[(r_x,r_y,r_z)], size=2, color=color.red)
    n += 1

