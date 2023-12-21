import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
from scipy import signal
import Myhilbert
matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
import os
Win=['hann','hamming','blackman','rect']
n=[51,100,151,200]
import soundfile as sf
# 指定文件夹路径
wave_name=['music1u-32.wav',
           'music2u-44.wav',
           'music3e-44.wav',
           'music4e-32.wav',
           'music5u-32.wav']
j=2#迭代次数
n=[51,100,151,200]
for fn in wave_name:
    folder_path = f"D:\Thr_1\FIR_github\wav_{fn}_{j}"
    # 使用os模块中的mkdir()函数创建文件夹
    os.mkdir(folder_path)
    for N in n:
        for win in Win:
            # 读取音频文件
            audio, samplerate = sf.read(fn)
            orthogonality_data, h = Myhilbert.hilbert(311, win, audio)
            # 设置滤波器参数
            cutoff_freq = 7000  # 设置截止频率为7kHz
            nyquist_freq = 0.5 * samplerate
            num_taps = N  # FIR滤波器阶数
            taps = signal.firwin(num_taps, cutoff_freq / nyquist_freq, window=win)  # 创建窗的FIR滤波器系数
            # 对音频数据进行滤波
            filtered_audio = signal.convolve(orthogonality_data.imag, taps, mode='same')
            # 将音频数据转换为整数类型
            filtered_audio = filtered_audio.astype(np.int16)
            #保存文件地址
            output_file = f"D:\Thr_1\FIR_github\wav_{fn}_{j}\{win}_阶数{N}_fir.wav"
            # 保存滤波后的音频文件
            sf.write(output_file, filtered_audio, samplerate)

