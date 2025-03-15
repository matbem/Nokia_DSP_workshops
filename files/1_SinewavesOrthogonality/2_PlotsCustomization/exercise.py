import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

t = np.linspace(0,2*2*np.pi,30,endpoint=False)

sin = 1.5*np.sin(t)

triangle = 3*signal.sawtooth(t,0.5)

sum_signal = sin + triangle

plt.figure()
plt.plot(t,sin,'p',label = "sinusoid", color = "blue")
plt.plot(t,triangle,'-p',label = "Teiangle",color = "green")
plt.plot(t,sum_signal,'--',color = "red", label = "sum")
plt.grid()
plt.xlabel("time")
plt.ylabel("amplitude")
plt.axhline(0,color = 'orange')
plt.xlim(0,10)
plt.ylim(-4,6)
plt.show()