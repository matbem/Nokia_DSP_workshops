import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# parameters
PERIOD_VECTOR_SIZE = 60

# loading Rx vector from file and..
Rx = np.load('TxSignal_exerc.npy')

# .. ploting it
plt.plot(Rx)
plt.grid()
plt.show()

# spliting vector into time slots coresponding to single periods
# "-1" causes automatic evaluation array seccond dimension  
RxPeriods = np.reshape(Rx,(-1,PERIOD_VECTOR_SIZE)) 

# lists for amplitudes
amplitudes_sin = []
amplitudes_cos = []

for RxPeriod in RxPeriods: # iterating periods    
    t = np.linspace(0, 2*pi,PERIOD_VECTOR_SIZE, endpoint=False)    
    # sinus amplitude evaluation
    ref_sin = np.sin(t)
    ampl_sin = 2*np.dot(RxPeriod,ref_sin)/PERIOD_VECTOR_SIZE
    amplitudes_sin.append(ampl_sin)
    # cosinus amplitude evaluation
    ref_cos = np.cos(t)
    ampl_cos = 2*np.dot(RxPeriod,ref_cos)/PERIOD_VECTOR_SIZE
    amplitudes_cos.append(ampl_cos)

# presentation
amplitudes_sin = np.array(amplitudes_sin) # convert list to numpy 1D array
amplitudes_cos = np.array(amplitudes_cos) # ...
np.set_printoptions(precision=2)          # set numpy array print precision
print(f'amplitudes_sin = {amplitudes_sin}')
print(f'amplitudes_cos = {amplitudes_cos}')



