import numpy as np
import matplotlib.pyplot as plt

def my_stem_plot(y,title,y_range=None):
    x = np.arange(len(y))    
    plt.stem(x,y,'-p')

    plt.xticks(x)
    
    if y_range:
        plt.ylim(y_range)
        plt.yticks(np.arange(*y_range))
    
    plt.grid()
    plt.title(title)
    fig = plt.gcf()
    fig.set_size_inches(4, 3.6)
    plt.show()
    

def myDTF(samples):
    
    SAMPLE_NR = len(samples)
    t = np.linspace(0, 2*np.pi, SAMPLE_NR, endpoint=False)
    
#    my_stem_plot(samples,f'samples, f_sig={SIN_FREQ}')
    
    real = list()
    imag = list()
    for f in range(SAMPLE_NR):
        real_part = 2*np.dot(samples,np.cos(f*t))/SAMPLE_NR
        imag_part = 2*np.dot(samples,np.sin(f*t))/SAMPLE_NR
        real.append(real_part)
        imag.append(imag_part)
    
    return real,imag