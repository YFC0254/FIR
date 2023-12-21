import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
import numpy as np
from scipy.signal import firwin, lfilter
import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import firwin, fftconvolve

# 读取音频文件
sample_rate, signal = wavfile.read('audio_file.wav')

# 设定滤波器的截止频率和过渡带宽度
cutoff = 4000  # 截止频率为4000Hz
transition_width = 1000  # 过渡带宽度为1000Hz

# 计算滤波器的长度
numtaps = int(4 * sample_rate / transition_width)

# 设计滤波器的系数
window = 'hann'  # 使用汉宁窗函数
filter_coeffs = firwin(numtaps, cutoff, fs=sample_rate, window=window)

# 对信号进行滤波
filtered_signal = fftconvolve(signal, filter_coeffs, mode='same')

# 绘制频谱图
spectrum = np.fft.fft(filtered_signal)
freq = np.fft.fftfreq(len(spectrum), d=1/sample_rate)

plt.plot(freq[:len(freq)//2], np.abs(spectrum[:len(freq)//2]))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Spectrum of Filtered Signal')
plt.grid(True)
plt.show()
