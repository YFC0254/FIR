# #10.2节
import numpy as np
# from scipy.signal import freqz, iirfilter
import matplotlib.pyplot as plt
import matplotlib
from scipy import signal
import Myhilbert
matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
# 汉字字体，优先使用楷体，找不到则使用黑体
plt.rcParams['font.sans-serif'] = ['Kaitt', 'SimHei']
# 正常显示负号
plt.rcParams['axes.unicode_minus'] = False
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
from scipy.signal import firwin, convolve
import soundfile as sf
# 读取音频文件
audio, samplerate = sf.read('music1u-32.wav')
win='hann'
orthogonality_data,h=Myhilbert.hilbert(311,win,audio)
# 设置滤波器参数
cutoff_freq = 7000  # 设置截止频率为7kHz
num_taps = 101  # FIR滤波器阶数
nyquist_freq = 0.5 * samplerate
taps = signal.firwin(num_taps, cutoff_freq / nyquist_freq, window='hamming')  # 创建Hamming窗口的FIR滤波器系数
# 对音频数据进行滤波
filtered_audio = signal.convolve(orthogonality_data.imag, taps, mode='same')
# 将音频数据转换为整数类型
filtered_audio = filtered_audio.astype(np.int16)
# 保存滤波后的音频文件
sf.write('output_fir.wav', filtered_audio, samplerate)
# 绘图
# 图一绘制正交移相器的时域和频域
plt.figure(1)
plt.subplot(2,1,1)
plt.title(f'{win}窗函数，希尔伯特变换冲激响应')
plt.plot(h,label=f'{win}窗函数，希尔伯特变换冲激响应')
plt.subplot(2,1,2)
plt.plot(np.abs(np.fft.fft(h)),label=f'{win}窗函数，希尔伯特变换的幅频响应')
plt.plot(f'{win}窗函数，希尔伯特变换的幅频响应')
# 图二绘制原信号与滤波后信号的时域
plt.figure(2)
# plt.subplot(2,1,1)
plt.plot(np.arange(len(audio)),audio,label=f'原信号波形')
# plt.title(f'原信号波形')
# plt.subplot(2,1,2)
plt.plot(np.arange(len(orthogonality_data.imag)),orthogonality_data.imag,label=f'{win}窗正交滤波器，滤波信号的虚部（希尔伯特变换）')
# 添加图例
plt.legend()
# plt.title(f'{win}窗正交滤波器，滤波信号的虚部（希尔伯特变换）')
# 图三输出的复信号的频谱
fft_orthogonality_data=np.fft.fft(orthogonality_data)
abs_orthogonality_data=np.abs(fft_orthogonality_data)
plt.figure(3)
plt.subplot(2,2,1)
plt.plot(abs_orthogonality_data)
plt.title(f'{win}窗正相滤波器，复信号频谱,abs')
plt.subplot(2,2,2)
plt.title(f'{win}窗正相滤波器，复信号频谱')
plt.show()




