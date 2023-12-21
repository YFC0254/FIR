import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
# 汉字字体，优先使用楷体，找不到则使用黑体
plt.rcParams['font.sans-serif'] = ['Kaitt', 'SimHei']
# 正常显示负号
plt.rcParams['axes.unicode_minus'] = False
import matplotlib.pyplot as plt
import Myhilbert
import matplotlib
matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
import soundfile as sf
Win=['hann','hamming','blackman','rect']
filename1=['music1u-32.wav','music2u-44.wav','music3e-44.wav','music4e-32.wav','music5u-32.wav']
i=1
for fn in filename1:
    # 读取音频文件
    audio, samplerate = sf.read(fn)
    for win in Win:
        orthogonality_data, h = Myhilbert.hilbert(311, win, audio)
        # 图二绘制原信号与滤波后信号的时域
        plt.figure(i)
        plt.title(f'窗为：{win},音频为：{fn}')
        plt.plot(np.arange(len(audio)), audio, label=f'原信号波形')
        plt.plot(np.arange(len(orthogonality_data.imag)), orthogonality_data.imag,label=f'信号过正交滤波器')
        # 添加图例
        plt.legend()
        i=i+1
# #
# audio, samplerate = sf.read('music5u-32.wav')
# win='rect'
# orthogonality_data, h = Myhilbert.hilbert(311, win, audio)
# # 图二绘制原信号与滤波后信号的时域
# plt.figure(1)
# plt.title(f'窗为：{win},音频为：music5u-32.wav')
# plt.plot(np.arange(len(audio)), audio, label=f'原信号波形')
# plt.plot(np.arange(len(orthogonality_data.imag)), orthogonality_data.imag,label=f'信号过正交滤波器')
# # 添加图例
# plt.legend()
