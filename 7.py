import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
# import numpy as np
# import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
# 生成一个示例信号
t = np.linspace(0, 1, 1000, endpoint=False)
x = np.cos(2 * np.pi * 5 * t)  # 5Hz的余弦信号

# 设计希尔伯特变换器
analytic_signal = signal.hilbert(x)

# 引入延迟M
M = 10
delayed_analytic_signal = np.roll(analytic_signal, M)

# 绘制原始信号和希尔伯特变换后的信号（包括延迟）
plt.plot(t, x, label='Original signal')
plt.plot(t, delayed_analytic_signal.real, label='Real part of delayed analytic signal')
plt.plot(t, delayed_analytic_signal.imag, label='Imaginary part of delayed analytic signal')
plt.xlabel('Time')
plt.ylabel('Signal')
plt.legend()
plt.show()
dot_product = np.dot(delayed_analytic_signal.real, delayed_analytic_signal.imag)
if dot_product<1e-10:
    print(1)