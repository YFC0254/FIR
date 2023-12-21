import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use("Qt5Agg")  # 修改配置的后端 backend
import soundfile as sf
wavsignal, rt = sf.read('music1u-32.wav')
print(*wavsignal.shape)
# print("sampling rate = {} Hz, length = {} samples, channels = {}".format(rt, *wavsignal.shape))
fg=plt.figure(1)
plt.plot(wavsignal)
plt.show()


