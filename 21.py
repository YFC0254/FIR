import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
import numpy as np
import scipy.io.wavfile as wav
from scipy import signal

# 读取音频文件
sample_rate, audio_data = wav.read('music1u-32.wav')

# 设置滤波器参数
cutoff_freq = 7000  # 设置截止频率为7kHz
nyquist_freq = 0.5 * sample_rate
b, a = signal.butter(4, cutoff_freq / nyquist_freq, 'low')  # 创建4阶Butterworth低通滤波器

# 对音频数据进行滤波
filtered_audio = signal.filtfilt(b, a, audio_data)

# 将音频数据转换为整数类型
filtered_audio = filtered_audio.astype(np.int16)

# 保存滤波后的音频文件
wav.write('output_butterworth.wav', sample_rate, filtered_audio)
