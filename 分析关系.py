import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
import matplotlib
from scipy import signal
import Myhilbert
matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
# 汉字字体，优先使用楷体，找不到则使用黑体
plt.rcParams['font.sans-serif'] = ['Kaitt', 'SimHei']
# 正常显示负号
plt.rcParams['axes.unicode_minus'] = False
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
import soundfile as sf
# 读取音频文件
audio, samplerate = sf.read('music1u-32.wav')
Win=['hann','hamming','blackman','rect']
n=[51,100,151,200]
i=1
for win in Win:
    j = 1
    for N in n:
        orthogonality_data,h=Myhilbert.hilbert(N,win,audio)
        # 绘图
        # 绘制图
        fft_orthogonality_data=np.fft.fft(orthogonality_data)
        abs_orthogonality_data=np.abs(fft_orthogonality_data)
        plt.figure(i)
        plt.subplot(2,2,j)
        plt.plot(abs_orthogonality_data)
        plt.title(f'{win}窗正相滤波器，阶数：{N}')
        j=j+1
    i=i+1
plt.show()

