import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
import scipy.signal as signal
import scipy.io.wavfile as wavfile
# import matplotlib.pyplot as plt

# 读取音频文件
sample_rate, data = wavfile.read('music1u-32.wav')

# 设计不同窗函数的正交移相器
windows = ['boxcar', 'hann', 'hamming', 'blackman']
for window in windows:
    # 应用窗函数
    window_func = signal.get_window(window, len(data))
    windowed_data = data * window_func

    # 使用 Hilbert 变换得到正交信号
    analytic_signal = signal.hilbert(windowed_data)
    amplitude_envelope = np.abs(analytic_signal)

    # 绘制频谱
    plt.magnitude_spectrum(amplitude_envelope, Fs=sample_rate, scale='dB')
    plt.title('Frequency Spectrum with ' + window + ' window')
    plt.show()
