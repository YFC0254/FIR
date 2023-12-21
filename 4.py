import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
import soundfile as sf
# # 读取音频文件
# audio, samplerate = sf.read('music1u-32.wav')

# fft_au=np.fft.fft(audio)
# M=len(fft_au)
# Omiga=2*np.pi*samplerate*np.arange(M)/M
# plt.plot(Omiga,abs(fft_au))
# plt.show()




import wave
import numpy as np
import matplotlib.pyplot as plt

# 打开.wav文件
with wave.open('music1u-32.wav', 'r') as wf:
    # 读取音频数据
    audio_data = wf.readframes(wf.getnframes())
    audio_data = np.frombuffer(audio_data, dtype=np.int16)  # 将数据转换为numpy数组

    # 获取采样频率
    samplerate = wf.getframerate()

# 绘制频谱图
plt.figure(figsize=(10, 4))
plt.specgram(audio_data, Fs=samplerate, NFFT=1024, noverlap=512, cmap='viridis')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.colorbar()
plt.show()
