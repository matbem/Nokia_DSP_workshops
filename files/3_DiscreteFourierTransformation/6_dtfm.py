import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from mylib import myDTF

# loads samples from .wav file with exemplary DTFM signal
# adapt file path 
samples = read(r'wav\d.wav')
samplig_freq = samples[0]
samples = samples[1]
samples = samples[:1024]
plt.plot(samples)
plt.show()

samples = samples - np.mean(samples)
# use commenst to swith between myDTF and numpy DTF (FFT)
#fft = np.fft.fft(samples)
#real = fft.real
#imag = fft.imag
real, imag = myDTF(samples)

plt.plot(real,label='real')
plt.plot(imag,label='imag')
plt.grid()
plt.legend()
plt.show()

#to show on freq scale

freq = np.linspace(0,samplig_freq,len(samples),endpoint=False)
real = np.array(real)
imag = np.array(imag)
magnitude = np.sqrt(real**2+imag**2)
plt.plot(freq,magnitude)
plt.grid()
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.show()

#culd be usefool for zooming
# plt.xlim(0,100)
# plt.ylim(-20_000,2_0000)






