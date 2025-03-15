import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60
TRANSMISION_NR = 10

AMPL_VECTOR_SIN = ( 1,-1, 1,-1)
AMPL_VECTOR_COS = ( 1, 1,-1,-1)


Noise_center = 0
Noise_deviation = 4

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

carrier_sin = ref_sin = np.sin(t) 
carrier_cos = ref_cos = np.cos(t) 

amplitudes_sin = list()
amplitudes_cos = list()

for i in range(TRANSMISION_NR):
    for j,(ampl_sin, ampl_cos) in enumerate(zip(AMPL_VECTOR_SIN, AMPL_VECTOR_COS)):
        
        # modulation
        Tx = (ampl_sin*carrier_sin) + (ampl_cos*carrier_cos)     
        
        # real channel
        Rx = Tx + np.random.normal(Noise_center,Noise_deviation,size=Tx.shape)
            
        # demodulation
        ampl_sin = (np.dot(Rx,ref_sin)/TIME_VECTOR_SIZE)*2  
        amplitudes_sin.append(ampl_sin)
        
        ampl_cos = (np.dot(Rx,ref_cos)/TIME_VECTOR_SIZE)*2  
        amplitudes_cos.append(ampl_cos)

        plt.scatter(ampl_cos,ampl_sin,color = (('red','orange','green','blue')[j%4]))
# PRESENTATION

# PRESENTATION  
# Rx plot

plt.axhline(y=0,lw=2, color = "black")
plt.axvline(x=0,lw=2,color="black")
plt.xlabel("cos ampl.")
plt.ylabel("sin ampl")
plt.xlim(-2,2)
plt.ylim(-2,2)
plt.grid()
plt.show()

# amplitudes
#amplitudes_sin = np.array(amplitudes_sin) # convert list to numpy 1D array
#amplitudes_cos = np.array(amplitudes_cos) # ...
#np.set_printoptions(precision=2)          # set numpy array print precision

#print(f'amplitudes_sin = {amplitudes_sin}')
#errors_sin = amplitudes_sin - AMPL_VECTOR_SIN
#print(f"errors sin: {errors_sin}")

#print(f"amplitudes_cos = {amplitudes_cos}")
#errors_cos = amplitudes_cos - AMPL_VECTOR_COS
#print(f"errors cos : {errors_cos}")

