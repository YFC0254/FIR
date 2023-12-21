import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
# import numpy as np
# import scipy.signal as signal
# import matplotlib.pyplot as plt
#
# # 设计参数
# fs = 44100  # 采样频率
# cutoff_frequency = 8000  # 截止频率
# Q = 30.0  # 品质因数
# frequencies = [9000, 14000]  # 要滤除的频率
#
# # 设计多阶低通滤波器
# order = 4  # 滤波器阶数
# b, a = signal.butter(order, 2 * cutoff_frequency / fs, 'low')
#
# # 在截止频率附近创建一个深谷
# for freq in frequencies:
#     w0 = freq / (0.5 * fs)
#     b, a = signal.iirnotch(w0, Q)
#
#
# # 绘制频率响应
# w, h = signal.freqz(b, a, worN=8000)
# plt.plot(0.5 * fs * w / np.pi, 20 * np.log10(np.abs(h)))
# plt.title('Multi-Stage Low-pass Filter Frequency Response')
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Gain (dB)')
# plt.grid(True)
# plt.show()
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# 设计参数
fs = 44100  # 采样频率
cutoff_frequency = 8000  # 截止频率
frequencies = [9000, 14000]  # 要滤除的频率

# 设计第一个滤波器（滤除9000Hz）
order = 4  # 滤波器阶数
b1, a1 = signal.butter(order, 2 * cutoff_frequency / fs, 'low')
w0_1 = frequencies[0] / (0.5 * fs)
b1_notch, a1_notch = signal.iirnotch(w0_1, 30.0)

# 设计第二个滤波器（滤除14000Hz）
b2, a2 = signal.butter(order, 2 * cutoff_frequency / fs, 'low')
w0_2 = frequencies[1] / (0.5 * fs)
b2_notch, a2_notch = signal.iirnotch(w0_2, 30.0)

# 将两个滤波器的系数相乘
b_cascade = np.convolve(b1, b1_notch) + np.convolve(b2, b2_notch)
a_cascade = np.convolve(a1, a1_notch) + np.convolve(a2, a2_notch)

# 绘制级联滤波器的频率响应
w, h = signal.freqz(b_cascade, a_cascade, worN=8000)
plt.plot(0.5 * fs * w / np.pi, 20 * np.log10(np.abs(h)))
plt.title('Cascade Filter Frequency Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)')
plt.grid(True)
plt.show()
