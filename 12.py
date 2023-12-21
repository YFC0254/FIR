import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# 设计参数
fs = 44100  # 采样频率
frequencies = [9000, 14000]  # 要滤除的干扰频率
num_taps = 101  # 滤波器阶数

# 设计FIR滤波器
taps = signal.remez(num_taps, [0, frequencies[0]-1000, frequencies[0], frequencies[1], frequencies[1]+1000, 0.5*fs], [0, 1, 0], Hz=fs)

# 绘制频率响应
w, h = signal.freqz(taps, worN=8000)
plt.plot(0.5*fs*w/np.pi, 20*np.log10(np.abs(h)))
plt.title('FIR Filter Frequency Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)')
plt.grid(True)
plt.show()
