import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
from matplotlib.ticker import MultipleLocator

matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
import scipy.io.wavfile as wavfile
import scipy.signal as signal

#读取音频
sample_rate, data = wavfile.read('music1u-32.wav')
# 设计参数
delt=20

fs = sample_rate  # 采样频率
f_cutoff1 = 9000-delt# 截止频率
f_cutoff2 = 9000+delt# 截止频率
f_cutoff3 = 14000-delt# 截止频率
f_cutoff4 = 14000+delt# 截止频率
f_cutoff5 = 15999# 截止频率
num_taps = 500*2*2*2*2  # 滤波器阶数
win='hamming'#boxcar,hann,hamming,blackman,triang,falttop
# 设计FIR低通滤波器
taps1 = signal.firwin(num_taps, f_cutoff1, fs=fs,window=win)
taps2 = signal.firwin(num_taps, f_cutoff2, fs=fs,window=win)
taps3 = signal.firwin(num_taps, f_cutoff3, fs=fs,window=win)
taps4 = signal.firwin(num_taps, f_cutoff4, fs=fs,window=win)
taps5 = signal.firwin(num_taps, f_cutoff5, fs=fs,window=win)

taps_end=taps1+taps3-taps2+taps5-taps4
#信号过滤波器
result=np.convolve(data,taps_end,mode='same')
#
# # 绘制频率响应
# plt.figure(1)
# ax=plt.gca()
# y_major_locator=MultipleLocator(5)#以每5显示
# ax.yaxis.set_major_locator(y_major_locator)
# w, h = signal.freqz(taps_end, worN=8000)
# plt.plot(0.5*fs*w/np.pi, 20*np.log10(np.abs(h)),callable(win))
# plt.title('FIR Lowpass Filter Frequency Response')
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Gain (dB)')
# plt.grid(True)
# plt.show()
# 绘制滤波前后的频谱图
plt.figure(2)
plt.figure(figsize=(10, 8))
plt.subplot(2, 1, 1)
plt.specgram(data, Fs=fs, NFFT=1024, noverlap=512, cmap='viridis')
plt.title('Original Audio')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.colorbar()
amplitude_envelope = np.abs(result)
plt.subplot(2, 1, 2)
plt.specgram(amplitude_envelope, Fs=fs, NFFT=1024, noverlap=512, cmap='viridis')
plt.title('Filtered Audio with Hilbert Transform')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.colorbar()

plt.tight_layout()
plt.show()

# 创建一个新的音频文件，并按照新的参数写入音频数据
wavfile.write('new5.wav', sample_rate, result)