import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
import librosa
import soundfile as sf

# 读取音频文件
y, sr = librosa.load('music1u-32.wav')

# 设计并应用滤波器
y_filtered = librosa.effects.preemphasis(y)

# 保存滤波后的音频文件
sf.write('audio_filtered.wav', y_filtered, sr)
