# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import *

if __name__ == '__main__':
    x = np.array([0.0, 0.5, 1.0, 6.0, 7.0, 9.0], dtype=np.float64)
    y = np.array([0.0, 1.6, 2.0, 1.5, 1.5, 0.0], dtype=np.float64)
    f5 = lagrange(x, y)
    tck = splrep(x, y)

    print(f5)
    print(tck[1])

    t = np.linspace(0, 10, 1000)
    c5 = f5(t)
    c3 = splev(t, tck)

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.plot(x, y, color='m', linestyle='', marker='o', label='给定数据')
    plt.plot(t, c5, color='b', linestyle='-', marker='', label="拉格朗日插值曲线")
    plt.plot(t, c3, color='g', linestyle='-', marker='', label="三次样条插值曲线")
    plt.legend(loc='best')
    plt.show()
