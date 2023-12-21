import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
import numpy as np
from scipy.signal import firwin, freqz,lfilter
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
sample_rate, audio_data = wav.read('music1u-32.wav')
# 指定采样率和截止频率
# sample_rate = 44100  # 采样率
cutoff_freq = 7000  # 截止频率（Hz）

# 计算滤波器阶数
nyquist_freq = 0.5 * sample_rate
num_taps = int(6.6 * sample_rate / cutoff_freq) + 1

# 设计汉明窗的FIR滤波器
taps = firwin(num_taps, cutoff_freq/nyquist_freq, window='hamming')
filtered_signal = lfilter(taps, 1.0, audio_data)
# 绘制滤波器的频率响应曲线
w, h = freqz(taps)
frequencies = w * nyquist_freq / np.pi
plt.plot(frequencies, 20 * np.log10(abs(h)))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)')
plt.title('Frequency Response')
plt.grid(True)
plt.show()
# 保存滤波后的音频文件
wav.write('output5.wav', sample_rate, filtered_signal)
