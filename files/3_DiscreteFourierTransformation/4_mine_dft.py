import numpy as np
import matplotlib.pyplot as plt
from mylib import my_stem_plot,myDTF

SAMPLE_NR = 10
SIN_FREQ = 3 
t = np.linspace(0, 2*np.pi, SAMPLE_NR, endpoint=False)
samples =  np.cos(t*SIN_FREQ)

real,imag = myDTF(samples)
my_stem_plot(real, "real")
my_stem_plot(imag, "imag")




