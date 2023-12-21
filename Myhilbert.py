import numpy as np
def hilbert(N,win, data):#N是正交移相器的阶数,win-窗类型，data-音频
    Nw=N
    # 窗函数
    if( win=='rect'):
        window=win_rect = np.ones(Nw)  # 矩形窗函数
    if win=='hann':
        window= np.hanning(Nw)  # 海宁窗函数
    if win=='blackman':
        window = np.blackman(Nw)  # 布莱克曼窗函数
    if win=='hamming':
        window = np.hamming(Nw)  # 汉明窗函数
    # 正交移相器
    wins = np.concatenate((window, np.zeros(N - Nw)))
    h = np.zeros(N)
    m = int((N - 1) / 2)
    h[0:N:2] = 2 / (((np.arange(0, N, 2)) - m) * np.pi)
    h = h * wins
    signal_delayed = np.roll(data, N // 2)
    i = np.convolve(signal_delayed, h, mode='same')
    result = signal_delayed + 1j * i
    return result ,h