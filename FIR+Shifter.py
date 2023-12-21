import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
import Shifter
import scipy.io.wavfile as wavfile

# 设计希尔伯特变换器
num_taps = 5
hamming_hilbert = Shifter.design_hilbert_transformer('hann', num_taps)
#读取音频
sample_rate, data = wavfile.read('music1u-32.wav')
# 生成输入信号
input_signal = data

# 将信号通过希尔伯特变换器
real_part, imag_part = Shifter.apply_hilbert_transform(input_signal, hamming_hilbert)
analytic_signal=real_part+1j*imag_part
amplitude_envelope = np.abs(analytic_signal)
# 确保输出信号是正交的
orthogonal_signal = np.dot(real_part, imag_part)
if orthogonal_signal<1e-10:
    print('正交')

# 绘制滤波前后的频谱图
plt.figure(figsize=(10, 8))
plt.subplot(2, 1, 1)
plt.specgram(data, Fs=sample_rate, NFFT=1024, noverlap=512, cmap='viridis')
plt.title('Original Audio')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.colorbar()

plt.subplot(2, 1, 2)
plt.specgram(amplitude_envelope, Fs=sample_rate, NFFT=1024, noverlap=512, cmap='viridis')
plt.title('Filtered Audio with Hilbert Transform')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.colorbar()

plt.tight_layout()
plt.show()
