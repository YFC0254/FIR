import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
# import numpy as np
# import matplotlib.pyplot as plt
from scipy.signal import firwin, convolve

# 1.设计希尔伯特变换滤波器
def hilbert_filter(N):
    h = np.zeros(N)
    for n in range(N):
        if n != N//2:
            h[n] = 1/(np.pi*(n-N//2))
    return h

# 2.生成输入信号
t = np.linspace(0, 1, 1000)
x = np.sin(2 * np.pi * 5 * t)
sig=x
# 3.应用希尔伯特变换滤波器
N = 30
# M=101
h = hilbert_filter(N)
hanning_window = np.hanning(N)
h1=hanning_window*h
#4.卷积
y = convolve(x, h1, mode='same')



# 5.绘制原始信号和希尔伯特变换后的信号
plt.figure()
plt.plot(t, x, label='Original signal')
plt.plot(t, y, label='Hilbert transformed signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
