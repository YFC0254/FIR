# #10.2节
import numpy as np
# from scipy.signal import freqz, iirfilter
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
# 汉字字体，优先使用楷体，找不到则使用黑体
plt.rcParams['font.sans-serif'] = ['Kaitt', 'SimHei']
# 正常显示负号
plt.rcParams['axes.unicode_minus'] = False

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use("Qt5Agg")  # 修改配置的后端 backend

from scipy.signal import firwin, convolve
#
# # 1.设计希尔伯特变换滤波器
# def hilbert(N):#N=8，N//2=4
#     h = np.zeros(N)
#     for n in range(N):
#         if n != N//2:
#             h[n] = 1/(np.pi*(n-N//2))
#     return h
#
# # 2.生成输入信号
# t = np.linspace(0, 1, 1000)
# x = np.sin(2 * np.pi * 5 * t)
# sig=x
# # 3.应用希尔伯特变换滤波器
# N = 16
# # M=101
# h = hilbert_filter(N)
# hanning_window = np.hanning(N)
# h1=hanning_window*h
# #4.卷积
# y = convolve(x, h1, mode='same')



# # 5.绘制原始信号和希尔伯特变换后的信号
# plt.figure()
# plt.plot(t, x, label='Original signal')
# plt.plot(t, y, label='Hilbert transformed signal')
# plt.xlabel('Time')
# plt.ylabel('Amplitude')
# plt.legend()
# plt.show()
import numpy as np
import matplotlib.pyplot as plt
# N = 64  # 选择滤波器长度
# t = np.linspace(0, 1, N, endpoint=False)  # 时间范围

# 创建一个信号
# x = np.sin(2 * np.pi * 5 * t)

# 创建希尔伯特变换滤波器系数h
def hilbert(N):
    h = np.zeros(N)
    for n in range(N):
         if n != N//2:
            h[n] = 1/(np.pi*(n-N/2))
    return h
# han=np.hanning(N)
# hx=han*h
# # 对信号进行希尔伯特变换
# x_hilbert = np.convolve(x, hx, mode='same')
#
# # 对x进行时移操作，使得其时延N/2后的信号与x_hilbert正交
# x_delayed = np.roll(x, N//2)
#
# # 计算内积得到正交条件
# inner_product = np.dot(x_hilbert, x_delayed)
#
# # 将x_hilbert和经过时移的x进行卷积，得到滤波后的信号y
# y = np.convolve(x_hilbert, x_delayed, mode='same')
#
# # 绘制结果
# plt.plot(t, x_delayed, label='原始信号')
# plt.plot(t, y, label='滤波后的信号')
# plt.legend()
# plt.show()
#
# # 输出内积结果
# print('内积结果：', inner_product)
