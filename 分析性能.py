import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
from scipy import signal
# import Myhilbert
import soundfile as sf
matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
# 汉字字体，优先使用楷体，找不到则使用黑体
plt.rcParams['font.sans-serif'] = ['Kaitt', 'SimHei']
# 正常显示负号
import numpy as np
def hilbert(N,win, data):#N是正交移相器的阶数,win-窗类型，data-音频
    Nw=N
    # 窗函数
    if( win=='rect'):
        window=win_rect = np.ones(Nw)  # 矩形窗函数
    if win=='hann':
        window= np.hanning(Nw)  # 海宁窗函数
    if win=='blackman':
        window = np.blackman(Nw)  # 布莱克曼窗函数
    if win=='hamming':
        window = np.hamming(Nw)  # 汉明窗函数
    # 正交移相器
    wins = np.concatenate((window, np.zeros(N - Nw)))
    h = np.zeros(N)
    m = int((N - 1) / 2)
    h[0:N:2] = 2 / (((np.arange(0, N, 2)) - m) * np.pi)
    h = h * wins
    signal_delayed = np.roll(data, N // 2)
    i = np.convolve(signal_delayed, h, mode='same')
    result = signal_delayed + 1j * i
    return h
audio, samplerate = sf.read('music1u-32.wav')
plt.rcParams['axes.unicode_minus'] = False
Win=['hann','hamming','blackman','rect']
n=[51,100,151,200]
i=1
for win in Win:
    j = 1
    for N in n:
        # 绘图
        # 绘制图
        h = hilbert(N, win, audio)
        plt.figure(i)
        plt.subplot(2,2,j)
        h=hilbert(N,win,audio)
        h=np.abs(np.fft.fft(h))
        h=np.array(20*np.log10(h))
        plt.plot(np.arange(len(h)),h)
        plt.title(f'{win}窗正相滤波器，阶数：{N}')
        plt.ylabel('增益(dB)')
        j=j+1
    i=i+1
plt.show()




