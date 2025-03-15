import numpy as np
import matplotlib.pyplot as plt
from mapper_lib import symbol_to_ampl,ampl_to_symbol

SYMBOL_NR = 8

amplitudes = np.linspace(-1.5,1.5,100,endpoint = False)

symbols_l = list()

for amplitude in amplitudes:
    symbol = ampl_to_symbol(SYMBOL_NR, amplitude)
    symbols_l.append(symbol)    

plt.plot(amplitudes,symbols_l,'p')    
plt.grid()
plt.title(f'Symbol nr: {SYMBOL_NR}')
plt.xlabel('Amplitude')
plt.ylabel('Symbol')
plt.show()

