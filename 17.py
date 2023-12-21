import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 设计FIR滤波器
fs = 32000  # 采样频率
nyquist = 0.5 * fs
cutoff_low = 50  # 通带截止频率
cutoff_high = 200  # 阻带截止频率
numtaps = 101  # 滤波器长度

# 设计低通FIR滤波器
taps_low = signal.firwin(numtaps, cutoff_low/nyquist)

# 设计带通FIR滤波器
taps_band = signal.firwin(numtaps, [cutoff_low/nyquist, cutoff_high/nyquist], pass_zero=False)

# 绘制滤波器的频率响应
plt.figure()
plt.plot(np.arange(numtaps), taps_low, label='Low Pass Filter')
plt.plot(np.arange(numtaps), taps_band, label='Band Pass Filter')
plt.xlabel('Filter Coefficients')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
