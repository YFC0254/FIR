import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
# import numpy as np
import scipy.signal as signal


# 设计希尔伯特变换器
def design_hilbert_transformer(window_type, num_taps):
    # 选择窗函数
    if window_type == 'hamming':
        window = signal.hamming(num_taps)
    elif window_type == 'hann':
        window = signal.hann(num_taps)
    elif window_type == 'blackman':
        window = signal.blackman(num_taps)
    else:
        raise ValueError('Unsupported window type')

    # 设计希尔伯特变换器
    h = np.zeros(num_taps)
    for n in range(num_taps):
        if n == num_taps // 2:
            h[n] = 0
        else:
            h[n] = np.sin(np.pi * (n - num_taps // 2)) / (np.pi * (n - num_taps // 2)) * window[n]

    return h


# 将信号通过希尔伯特变换器
def apply_hilbert_transform(input_signal, hilbert_coeffs):
    # 使用滤波器系数进行滤波
    filtered_signal = np.convolve(input_signal, hilbert_coeffs, mode='same')

    # 希尔伯特变换后的实部和虚部
    real_part = input_signal
    imag_part = filtered_signal

    return real_part, imag_part

