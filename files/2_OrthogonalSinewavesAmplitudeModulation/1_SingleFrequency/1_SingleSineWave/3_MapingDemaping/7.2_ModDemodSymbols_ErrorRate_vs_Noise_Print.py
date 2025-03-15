import numpy as np
import matplotlib.pyplot as plt
from mapper_lib import symbol_to_ampl, ampl_to_symbol 

# PARAMETERS
TIME_VECTOR_SIZE = 60
TRANSMISIONS_NR = 1000

NOISE_CENTER = 0
NOISE_DEVIATION = [0.00, 0.22, 0.44, 0.67, 0.89, 1.11, 1.33, 1.56, 1.78, 2.00]
SYMBOL_NR = 8

t = np.linspace(0, 2*np.pi,TIME_VECTOR_SIZE, endpoint=False)
Carrier = np.sin(t) 
Ref     = Carrier
errors = np.array([])

# TRANSMISION-RECEPTION
symbols_tx = np.random.randint(0,SYMBOL_NR,TRANSMISIONS_NR)   

for dev in NOISE_DEVIATION: 
    symbols_rx = list()
    for symbol in symbols_tx:        
        # modulation
        ampl = symbol_to_ampl(SYMBOL_NR, symbol)
        Tx = ampl*Carrier        
        # real channel
        Rx = Tx + np.random.normal(NOISE_CENTER,dev,size = Tx.shape)  
        # demodulation
        ampl = (np.dot(Rx,Ref)/TIME_VECTOR_SIZE)*2  
        symbol = ampl_to_symbol(SYMBOL_NR, ampl)
    
        symbols_rx.append(symbol)

# PRESENTATION   
    symbols_rx = np.array(symbols_rx) # list to numpy array
    errors = np.append(errors,sum(symbols_tx != symbols_rx))

print(f"symbol number = {SYMBOL_NR}")
print("noise dev : error nr")

for dev,err in zip(NOISE_DEVIATION,errors):
    print(f"{dev} : {err}")
# print('symbols_rx')    
#print('\n symbols_rx\n:', symbols_tx)
#errors = symbols_rx != symbols_tx
#print('\n errors:\n', errors)
#print('\n errors nr:', sum(symbols_rx != symbols_tx))



