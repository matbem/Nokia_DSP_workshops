import numpy as np
import matplotlib.pyplot as plt
from mapper_lib import symbol_to_ampl, ampl_to_symbol 

# PARAMETERS
TIME_VECTOR_SIZE = 60
TRANSMISIONS_NR = 1000

NOISE_DEVIATION = [0.0,0.22,0.44,0.67,0.89,1.11,1.33,1.56,1.78,2.0]
SYMBOL_NR = 4

t = np.linspace(0, 2*np.pi,TIME_VECTOR_SIZE, endpoint=False)
carrier_sin = ref_sin = np.sin(t) 
carrier_cos = ref_cos = np.cos(t) 

# TRANSMISION-RECEPTION
symbols_tx_sin = np.random.randint(0,SYMBOL_NR,TRANSMISIONS_NR)  
symbols_tx_cos = np.random.randint(0,SYMBOL_NR,TRANSMISIONS_NR)  

print(f"SYMBOL_NR: {SYMBOL_NR}")
print("DEV: SIN, COS")

for deviation in NOISE_DEVIATION:
    symbols_rx_sin = list()
    symbols_rx_cos = list()
    for symbol_sin, symbol_cos in zip(symbols_tx_sin,symbols_tx_cos):        
        # modulation
        ampl_sin = symbol_to_ampl(SYMBOL_NR, symbol_sin)
        ampl_cos = symbol_to_ampl(SYMBOL_NR, symbol_cos)
        Tx = (ampl_sin*carrier_sin) + (ampl_cos*carrier_cos)
        # real channel
        Rx = Tx + np.random.normal(loc=0, scale=deviation, size=len(Tx))    
        # demodulation
        ampl_sin = 2*np.dot(Rx,ref_sin)/TIME_VECTOR_SIZE        
        ampl_cos = 2*np.dot(Rx,ref_cos)/TIME_VECTOR_SIZE
        
        symbol_sin = ampl_to_symbol(SYMBOL_NR, ampl_sin)
        symbol_cos = ampl_to_symbol(SYMBOL_NR, ampl_cos)
        
        symbols_rx_sin.append(symbol_sin)
        symbols_rx_cos.append(symbol_cos)

    # PRESENTATION   
    symbols_rx_sin = np.array(symbols_rx_sin) # list to numpy array
    symbols_rx_cos = np.array(symbols_rx_cos)
    

    errors_sin = symbols_rx_sin != symbols_tx_sin
    errors_cos = symbols_rx_cos != symbols_tx_cos
    
    print(f"{deviation}: {sum(errors_sin)}: {sum(errors_cos)}")



