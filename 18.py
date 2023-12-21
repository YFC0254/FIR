import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, firwin, lfilter
from scipy.io import wavfile
import sounddevice as sd
from scipy.signal import spectrogram
from scipy.signal.windows import hamming

# 读取音频文件
Fs32, x32 = wavfile.read('music4e-32.wav')
N = len(x32)

# 观察输入音频
plt.figure(1)
plt.subplot(2, 1, 1)
plt.stem(x32)
plt.title('时域波形')
plt.subplot(2, 1, 2)
plt.plot(np.abs(np.fft.fft(x32)))
plt.title('FFT')
plt.grid(True)

# 设计正交移相器
N1 = 31  # 正交移相器阶数
M = (N1 - 1) // 2  # 延迟单元长度
h = np.zeros(N1)
h[0:N1:2] = 2 / (((np.arange(0, N1, 2) - M) * np.pi))
plt.figure(3)
freq, response = freqz(h)
plt.plot(freq, np.abs(response))
plt.grid(True)

# # 将输入信号延迟
# x1 = np.zeros(N + M)
# x1[M:N + M] = x32
x1 = np.roll(x32, M)
# 重叠相加法
# L = 120
# y2 = lfilter(h, 1, x32, axis=0)
# N1 = len(y2)
# y3 = np.zeros(N1)
# y3[:N1] = y2
y3=np.convolve(h,x1,mode='same')
plt.figure(4)
plt.stem(y3)
plt.title('经过正交移相器后输出')
plt.grid(True)

# 观察复信号频谱
N2 = len(x1)
x2 = np.zeros(N2)
x2[:N2] = x1
N3 = min(N1, N2)
y4 = x2[:N3] + 1j * y3[:N3]
plt.figure(5)
plt.plot(np.abs(np.fft.fft(y4)))
plt.title('复信号频谱')

# 设置FIR低通滤波器
fp = 7000  # 通带截止频率
fs = 8000  # 阻带截止频率
rs = 60  # 阻带最小衰减
wp = 2 * np.pi * fp / Fs32
ws = 2 * np.pi * fs / Fs32
Bt = ws - wp
alph = 0.5842 * (rs - 21) ** 0.4 + 0.07886 * (rs - 21)
M = int(np.ceil((rs - 8) / (2.285 * Bt)))  # 计算滤波器阶数
wc = (wp + ws) / 2  # 理想低通滤波器的通带截止频率
hn = firwin(M + 1, wc / np.pi, window=('kaiser', alph))
C1 = 20 * np.log10(np.abs(np.fft.fft(hn, 2048)) / max(np.abs(np.fft.fft(hn, 2048))))
y5 = np.convolve(hn, y4)
y6 = np.fft.fft(y5)

plt.figure(6)
plt.subplot(2, 1, 1)
plt.stem(hn)
plt.title('hn波形')
plt.subplot(2, 1, 2)
plt.plot(C1)
plt.title('滤波器幅频特性')

plt.figure(7)
plt.plot(np.abs(y6))
plt.title('复信号经滤波器输出')
plt.grid(True)

plt.figure(8)
freq, response = freqz(y5)
plt.plot(freq, np.abs(response))
plt.grid(True)

sd.play(y5.astype(np.int16), Fs32)

# 语谱图
window = hamming(512)  # 窗函数
window=np.squeeze(window)
noverlap = 256  # 重叠的采样点数
nfft = 1024  # FFT长度
f, t, p = spectrogram(y5, window, noverlap, nfft, Fs32)
plt.figure(9)
plt.pcolormesh(t, f, 10 * np.log10(p), shading='gouraud')
plt.xlabel('Time')
