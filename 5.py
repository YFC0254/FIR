import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
import hilberts
matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
import wave
# import numpy as np
from scipy.signal import hilbert, firwin, lfilter
# import matplotlib.pyplot as plt
import soundfile as sf
# 打开.wav文件
with wave.open('music1u-32.wav', 'r') as wf:
    # 读取音频数据
    audio_data = wf.readframes(wf.getnframes())
    audio_data = np.frombuffer(audio_data, dtype=np.int16)  # 将数据转换为numpy数组

    # 获取采样频率
    samplerate = wf.getframerate()

# 设计希尔伯特变换滤波器
filter_length = 101  # 滤波器长度
filter_order = filter_length - 1  # 滤波器阶数
nyquist_rate = samplerate / 2.0  # 奈奎斯特频率
cutoff_freq1 = 9000.0  # 截止频率1
cutoff_freq2 = 14000.0  # 截止频率2

# 使用不同窗函数设计希尔伯特变换滤波器
fir_filter1 = firwin(filter_length, cutoff_freq1/nyquist_rate, window='hann', pass_zero='lowpass')
fir_filter2 = firwin(filter_length, [cutoff_freq1/nyquist_rate, cutoff_freq2/nyquist_rate], window='hamming', pass_zero='bandpass')
N=500
h=hilberts.hilbert(N)
han=np.hanning(N)
hx=han*h
# 将两个滤波器合并为一个希尔伯特变换滤波器
fir_filter = np.vstack((fir_filter1, fir_filter2))

# 对音频数据进行滤波
filtered_audio1 = lfilter(fir_filter1, 1.0, audio_data)
filtered_audio2 = lfilter(fir_filter2, 1.0, audio_data)
filtered_audio3=lfilter(hx, 1.0, audio_data)
# 计算希尔伯特变换
analytic_signal = hilbert(filtered_audio1)
amplitude_envelope = np.abs(analytic_signal)

# 绘制滤波前后的频谱图
plt.figure(figsize=(10, 8))
plt.subplot(2, 1, 1)
plt.specgram(audio_data, Fs=samplerate, NFFT=1024, noverlap=512, cmap='viridis')
plt.title('Original Audio')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.colorbar()

plt.subplot(2, 1, 2)
plt.specgram(amplitude_envelope, Fs=samplerate, NFFT=1024, noverlap=512, cmap='viridis')
plt.title('Filtered Audio with Hilbert Transform')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.colorbar()

plt.tight_layout()
plt.show()

# 创建一个新的音频文件，并按照新的参数写入音频数据
sf.write('new_music.wav', filtered_audio3, 16000*2)  # 以16000Hz的采样频率写入新文件