import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# 定义采样频率和时间向量
fs = 100000  # 采样率（Hz）
T = 1/fs  # 采样时间
t = np.arange(0, 1, T)  # 时间向量

# 生成带有9 kHz和14 kHz干扰的测试信号
f1 = 9000  # 干扰1（9 kHz）的频率
f2 = 14000  # 干扰2（14 kHz）的频率
x = 0.5*np.sin(2*np.pi*5000*t) + np.sin(2*np.pi*f1*t) + 0.5*np.sin(2*np.pi*f2*t)

# 设计带阻滤波器以消除9 kHz和14 kHz处的干扰
nyq = 0.5 * fs
f0 = [8000, 9200]  # 9 kHz处带阻滤波器的截止频率
f1 = [13500, 14500]  # 14 kHz处带阻滤波器的截止频率
b, a = signal.butter(4, [f0[0]/nyq, f0[1]/nyq], btype='bandstop')
x_filtered_9k = signal.filtfilt(b, a, x)
b, a = signal.butter(4, [f1[0]/nyq, f1[1]/nyq], btype='bandstop')
x_filtered_14k = signal.filtfilt(b, a, x_filtered_9k)

# 应用希尔伯特变换
x_hilbert = signal.hilbert(x_filtered_14k)
# 确保输出信号是正交的
orthogonal_signal = np.dot(x_hilbert.real, x_hilbert.imag)
# 绘制原始信号和处理后的信号
plt.figure()
plt.plot(t, x, label='原始信号')
plt.plot(t, x_hilbert.real, label='希尔伯特变换后的实部')
plt.plot(t, x_hilbert.imag, label='希尔伯特变换后的虚部')
plt.xlabel('时间 [s]')
plt.ylabel('幅度')
plt.legend()
plt.show()
