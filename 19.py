import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
# import numpy as np
# from scipy import signal
# import matplotlib.pyplot as plt
#
# # 生成一个简单的信号
# Fs = 1000  # 采样频率
# t = np.arange(0, 1, 1/Fs)  # 时间向量
# f = 5  # 信号频率
# x = np.sin(2 * np.pi * f * t)  # 生成正弦波信号
#
# # 设计理想低通滤波器
# cutoff_freq = 10  # 截止频率
# num_taps = 101  # 滤波器系数的数量
# lpf = signal.firwin(num_taps, cutoff_freq, fs=Fs, pass_zero=True)
#
# # 应用滤波器
# filtered_x = signal.lfilter(lpf, 1.0, x)
#
# # 绘制原始信号和滤波后的信号
# plt.plot(t, x, label='Original Signal')
# plt.plot(t, filtered_x, label='Filtered Signal')
# plt.xlabel('Time')
# plt.ylabel('Amplitude')
# plt.legend()
# plt.show()
import numpy as np
import scipy.io.wavfile as wav

# 读取音频文件
sample_rate, audio_data = wav.read('music1u-32.wav')

# 获取音频数据长度
num_samples = len(audio_data)

# 对音频进行傅里叶变换
fft_data = np.fft.fft(audio_data)

# 计算频率分辨率
freq_res = sample_rate / num_samples

# 确定需要滤除的频率范围
cutoff_freq = 7000  # 设置为7kHz

# 计算截止频率对应的索引
cutoff_index = int(cutoff_freq / freq_res)

# 将滤波器前半部分置零（包括截止频率）
filtered_fft = np.concatenate((fft_data[:cutoff_index], np.zeros(len(fft_data) - cutoff_index)))

# 对滤波后的频域数据进行反傅里叶变换
filtered_audio = np.fft.ifft(filtered_fft)

# 提取实部作为滤波后的音频数据
filtered_audio = np.real(filtered_audio)

# 将音频数据转换为整数类型
filtered_audio = filtered_audio.astype(np.int16)

# 保存滤波后的音频文件
wav.write('output4.wav', sample_rate, filtered_audio)
