import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

import scipy.io.wavfile as wavfile
#读取音频
sample_rate, data = wavfile.read('music1u-32.wav')



# 设计希尔伯特变换器
def design_hilbert_transformer(num_taps, cutoff_freq, fs):
    # 设计希尔伯特变换器的FIR滤波器系数
    h = signal.firwin(num_taps, cutoff_freq, fs=fs, pass_zero=False, window='hann')

    return h

# 将信号通过希尔伯特变换器
def apply_hilbert_transform(input_signal, hilbert_coeffs):
    # 使用滤波器系数进行滤波
    filtered_signal = signal.lfilter(hilbert_coeffs, 1, input_signal)

    # 希尔伯特变换后的实部和虚部
    real_part = input_signal
    imag_part = filtered_signal

    return real_part, imag_part

# 采样频率和时间向量
fs = 100000  # 采样率（Hz）
T = 1/fs  # 采样时间
t = np.arange(0, 1, T)  # 时间向量

# 生成带有9 kHz和14 kHz干扰的测试信号
f1 = 9000  # 干扰1（9 kHz）的频率
f2 = 14000  # 干扰2（14 kHz）的频率
x = 0.5*np.sin(2*np.pi*5000*t) + np.sin(2*np.pi*f1*t) + 0.5*np.sin(2*np.pi*f2*t)

# 设计希尔伯特变换器的FIR滤波器系数
num_taps = 101  # FIR滤波器的阶数
cutoff_freq = [8500, 9500]  # 9 kHz处的截止频率
h = design_hilbert_transformer(num_taps, cutoff_freq, fs)

# 将信号通过希尔伯特变换器
real_part, imag_part = apply_hilbert_transform(x, h)
analytic_signal=real_part+1j*imag_part
amplitude_envelope = np.abs(analytic_signal)
# 绘制滤波前后的频谱图
plt.figure(figsize=(10, 8))
plt.subplot(2, 1, 1)
plt.specgram(data, Fs=fs, NFFT=1024, noverlap=512, cmap='viridis')
plt.title('Original Audio')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.colorbar()

plt.subplot(2, 1, 2)
plt.specgram(amplitude_envelope, Fs=fs, NFFT=1024, noverlap=512, cmap='viridis')
plt.title('Filtered Audio with Hilbert Transform')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.colorbar()
# 确保输出信号是正交的
orthogonal_signal = np.dot(real_part, imag_part)

plt.tight_layout()
plt.show()
