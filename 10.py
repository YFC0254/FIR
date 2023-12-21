import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
#读取音频
sample_rate, data = wavfile.read('music1u-32.wav')
# 定义采样频率和时间向量
fs = sample_rate  # 采样率（Hz）

x=data
# 设计带阻滤波器以消除9 kHz和14 kHz处的干扰
nyq = 0.5 * sample_rate
f0 = [8500, 9500]  # 9 kHz处带阻滤波器的截止频率
f1 = [13500, 14500]  # 14 kHz处带阻滤波器的截止频率
b, a = signal.butter(4, [f0[0]/nyq, f0[1]/nyq], btype='bandstop')
x_filtered_9k = signal.filtfilt(b, a, x)
b, a = signal.butter(4, [f1[0]/nyq, f1[1]/nyq], btype='bandstop')
x_filtered_14k = signal.filtfilt(b, a, x_filtered_9k)

analytic_signal = x_filtered_14k
amplitude_envelope = np.abs(analytic_signal)
fft_x=np.abs(np.fft.fft(x))
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

plt.tight_layout()
plt.show()

# 创建一个新的音频文件，并按照新的参数写入音频数据
wavfile.write('new.wav', sample_rate, data)