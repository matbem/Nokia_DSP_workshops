import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMS
TIME_VECTOR_SIZE = 30

A = 1
B = 1

# CALCULATIONS
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

Sin_A = A * np.sin(t)
Sin_B = B * np.sin(t)
dot = np.dot(Sin_A,Sin_B)

# PRESENTATION
print(f'A = {A}')
print(f'B = {B}')
print(f'dot = {dot:0.2f}')


