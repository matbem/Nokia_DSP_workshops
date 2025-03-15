import numpy as np
from mylib import rotate_vector

green = [0,1]

for alpha in range(0,370,10):
    blue = rotate_vector(green, alpha)
    dot = np.dot(green,blue)
    print(f"{alpha:03} : {dot:+3f}")