import numpy as np
import matplotlib.pyplot as plt
from mylib import my_stem_plot,myDTF

SAMPLE_NR = 10
FREQ = 1

t = np.linspace(0, 2*np.pi, SAMPLE_NR, endpoint=False)

samples =  np.sin(t*FREQ) 
my_stem_plot(samples,f'f={FREQ}')




