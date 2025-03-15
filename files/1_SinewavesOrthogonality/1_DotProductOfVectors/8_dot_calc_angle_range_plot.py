import numpy as np
from mylib import rotate_vector
import matplotlib.pyplot as plt

v = [0, 1]

angle_list = list()
dot_list = list()

for angle in range(0,370,10):    
    angle_list.append(angle)    
    v_rot = rotate_vector(v, angle)
    dot = np.dot(v,v_rot)
    dot_list.append(dot)

plt.plot(angle_list,dot_list)

plt.xlabel("Angle")
plt.ylabel("Dot product")
plt.axhline(0, color="black")
plt.grid()
plt.show()



