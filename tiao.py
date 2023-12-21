import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
# import numpy as np
import scipy.signal
from scipy import fftpack
import hilberts
import soundfile as sf
N=10
h=hilbert.hilbert(N)
hanningWin=np.hanning(N)
hn=hanningWin*h
# t = np.linspace(0, 1, 1000)#1
t=np.arange(50)
x = np.sin(2 * np.pi * 5 * t*0.0625)
x_delayed = np.roll(x, N//2)
y =np.convolve(x, hn, mode='same')
plt.plot(t,x,label='Original signal')
plt.plot(t,y,label='now signal')
plt.show()
