import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETER
PHASE_SHIFT = pi/8 

# VECTORS
t = np.linspace(0, 2*pi,30, endpoint=False)

Ref = np.sin(t)
Shifted = np.sin(t+PHASE_SHIFT)
Ref_mult_Shifted = Ref * Shifted
dot_product = np.sum(Ref_mult_Shifted) # use Ref_mult_Shifted

# PLOTS (HINT: use separate plots, not one with grid)
plt.figure()
plt.plot(t,Ref,'-p',color = 'blue',label = 'Ref')
plt.plot(t,Shifted,'-p', label = 'Shifted', color = 'green')
plt.title("Components")
plt.grid()
plt.axhline(y=0, color = "black", linewidth = 1.5)
plt.show()

plt.figure()
plt.stem(t,Ref_mult_Shifted,'o',markerfmt='ro',basefmt='r-', label = "Ref_mult_Shifted")
plt.grid()
plt.title("Multiplication")
plt.axhline(y= 0,color = "red", lw = 1.5)
plt.ylim(-1,1)
plt.show()
# components
...
# multiplication, HINT: use "stem" function for ploting
...
# print phase shift and dot product value
...

