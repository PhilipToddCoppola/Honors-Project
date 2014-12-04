from visual import *

sphereOne = sphere(pos=vector(-1, 0, 0), radius=0.25, color=color.green)
sphereTwo = sphere(pos=vector(1, 1, 0), radius=0.15, color=color.red)

arrow(pos=sphereOne.pos, axis=sphereTwo.pos-sphereOne.pos, color=color.red)
