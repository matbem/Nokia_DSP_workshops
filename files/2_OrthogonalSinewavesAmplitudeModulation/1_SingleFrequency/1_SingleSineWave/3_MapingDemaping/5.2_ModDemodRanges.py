import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60
AMPL_VECTOR = (1.2, -3.4, 4.5, -1.2)
Noise_center = 0
Noise_dev = 1
Transmission_nr = 100

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)
Rx_periods = np.array([])
Rx = 0
# modulation
Carrier = np.sin(t)
amplitude_list = np.array([]) # create amplitude list
for i in range(Transmission_nr):
    amp = AMPL_VECTOR[i%len(AMPL_VECTOR)]
    Tx = amp*Carrier
    Noise = np.random.normal(Noise_center,Noise_dev, size = Tx.shape)
    # channel
    Rx=Tx + Noise
    Rx_periods = np.append(Rx_periods,Rx)
    # demodulation
    Ref  = np.sin(t)    
    dot  = np.dot(Rx,Ref)
    ampl = 2*dot/TIME_VECTOR_SIZE
    amplitude_list = np.append(amplitude_list,ampl)

# PRESENTATION  

# Rx plot
plt.plot(amplitude_list,'o') 
plt.axhline(y=0,color='black')
plt.grid(axis='y')
plt.show()

#  
print(f'received amplitudes: {amplitude_list}')
#print(f"errors: {amplitude_list - AMPL_VECTOR}")