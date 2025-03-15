import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi,30, endpoint=False)
sin_blue  = np.sin(t)

dot_l = list()
freq_l = np.linspace(0, 3, 100)
for freq in freq_l:    
    sin_green = np.sin(freq*t)
    dot_l.append(np.dot(sin_blue,sin_green))
    
plt.plot(freq_l, dot_l)
plt.axhline(y=0,color='black')
plt.title('sin - dot of "blue" and "green" frequencies when "blue" frequency equals to 1')
plt.xlabel('"green" frequency')
plt.ylabel('dot')
plt.grid()
plt.show()


cos_blue  = np.cos(t)

dot_l = list()
freq_l = np.linspace(0, 3, 100)
for freq in freq_l:    
    cos_green = np.cos(freq*t)
    dot_l.append(np.dot(cos_blue,cos_green))
    
plt.plot(freq_l, dot_l)
plt.axhline(y=0,color='black')
plt.title('cos - dot of "blue" and "green" frequencies when "blue" frequency equals to 1')
plt.xlabel('"green" frequency')
plt.ylabel('dot')
plt.grid()
plt.show()