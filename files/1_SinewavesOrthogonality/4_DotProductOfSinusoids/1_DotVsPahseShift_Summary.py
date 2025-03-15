import numpy as np
import matplotlib.pyplot as plt

phase_shift = np.linspace(0,np.pi,30,endpoint = False)
t = np.linspace(0,2*np.pi,30, endpoint=False)

Ref = np.sin(t)
dot_products = np.array([])

for shift in phase_shift:
    shifted = np.sin(t+shift)
    dot = np.dot(Ref,shifted)
    dot_products = np.append(dot_products, dot)
    
plt.figure()
plt.plot(phase_shift,dot_products,'-p',color = 'blue')
plt.xlabel("shift")
plt.ylabel("dot")
plt.axhline(y=0,color = "black")
plt.grid()
plt.show()
