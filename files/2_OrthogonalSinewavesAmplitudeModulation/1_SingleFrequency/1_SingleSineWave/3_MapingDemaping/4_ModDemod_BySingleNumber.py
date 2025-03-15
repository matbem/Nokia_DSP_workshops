import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60
AMPL_VECTOR = (1.2, -3.4, 4.5, -1.2)

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)
Rx = 0
# modulation
Carrier = np.sin(t)
amplitude_list = [] # create amplitude list
for amp in AMPL_VECTOR:
    Tx = amp*Carrier

    # channel
    Rx=Tx # ideal one    

    # demodulation
    Ref  = np.sin(t)    
    dot  = np.dot(Rx,Ref)
    ampl = 2*dot/TIME_VECTOR_SIZE
    amplitude_list.append(ampl)

# PRESENTATION  

# Rx plot
plt.plot(Rx)
plt.axhline(y=0,color='black')
plt.grid(axis='y')
plt.show()

#  
print(f'received amplitudes: {amplitude_list}')


