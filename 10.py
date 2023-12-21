import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
import Myhilbert
fn='music1u-32.wav'
import soundfile as sf
win='hann'
N=311

# 读取音频文件
audio, samplerate = sf.read(fn)
orthogonality_data, h = Myhilbert.hilbert(311, win, audio)
# 设置滤波器参数
cutoff_freq = 7000  # 设置截止频率为7kHz
nyquist_freq = 0.5 * samplerate
num_taps = N  # FIR滤波器阶数
taps = signal.firwin(num_taps, cutoff_freq / nyquist_freq, window=win)  # 创建窗的FIR滤波器系数
# 对音频数据进行滤波
filtered_audio = signal.convolve(audio, taps, mode='same')
# 将音频数据转换为整数类型
filtered_audio = filtered_audio.astype(np.int16)
#保存文件地址
output_file = f"{win}_阶数{N}_fir_.wav"
# 保存滤波后的音频文件
sf.write(output_file, filtered_audio, samplerate)