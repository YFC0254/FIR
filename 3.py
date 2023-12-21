import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import soundfile as sf
# import numpy as np
# import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
Nw = 311
N = 311  # 正交移相器的阶数
M=(N-1)/2
# 窗函数
win_rect = np.ones(Nw)  # 矩形窗函数
win_hamming = np.hamming(Nw)  # 汉明窗函数
win_hann = np.hanning(Nw)  # 海宁窗函数
win_blackman = np.blackman(Nw)  # 布莱克曼窗函数

# 正交移相器
win_hamming = np.concatenate((win_hamming, np.zeros(N-Nw)))
h = np.zeros(N)
m = int((N-1)/2)
h[0:N:2] = 2/(((np.arange(0, N, 2))-m)*np.pi)
h = h*win_hamming



from scipy.io import wavfile

# plt.stem(h)
# plt.show()
sample_rate, data = wavfile.read('music1u-32.wav')
signal_delayed = np.roll(data, N//2)
i=np.convolve(signal_delayed,h,mode='same')
result=signal_delayed+1j*i
# plt.plot(np.arange(len(signal_delayed)),signal_delayed)
plt.plot(np.arange(len(i)),i)
hi=signal.hilbert(data)
plt.plot(np.arange(len(hi)),hi.imag)
plt.show()


