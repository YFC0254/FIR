import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
# import numpy as np
# import matplotlib.pyplot as plt
import soundfile as sf
from scipy.signal import hilbert, firwin, lfilter
# 参数设置
N = 64  # 滤波器长度
fs = 32100  # 采样频率
fc = 1000 # 通带边界频率
M = N-1  # 滤波器的阶数

# 理想希尔伯特变换滤波器的频率响应
H_ideal = np.zeros(N)
H_ideal[0:int(N/2)+1] = 1
H_ideal = H_ideal * 2
H_ideal[0] = 1

# 窗函数
w = np.hamming(N)

# 加窗
H = H_ideal * w

# 时域响应
h = np.fft.ifft(H)

# 绘制频率响应
plt.figure()
plt.plot(np.abs(np.fft.fft(H)))
plt.title('Frequency response')
plt.show()
import wave
# 打开.wav文件
with wave.open('music1u-32.wav', 'r') as wf:
    # 读取音频数据
    audio_data = wf.readframes(wf.getnframes())
    audio_data = np.frombuffer(audio_data, dtype=np.int16)  # 将数据转换为numpy数组

    # 获取采样频率
    samplerate = wf.getframerate()
filtered_audio3=lfilter(h, 1.0, audio_data)
# 创建一个新的音频文件，并按照新的参数写入音频数据
# sf.write('new_music5.wav', filtered_audio3, 16000*2)  # 以16000Hz的采样频率写入新文件


# 绘制滤波前后的频谱图
plt.figure(figsize=(10, 8))
plt.subplot(2, 1, 1)
plt.specgram(audio_data, Fs=samplerate, NFFT=1024, noverlap=512, cmap='viridis')
plt.title('Original Audio')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.colorbar()
amplitude_envelope = np.abs(filtered_audio3)
plt.subplot(2, 1, 2)
plt.specgram(amplitude_envelope, Fs=samplerate, NFFT=1024, noverlap=512, cmap='viridis')
plt.title('Filtered Audio with Hilbert Transform')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.colorbar()

plt.tight_layout()
plt.show()
