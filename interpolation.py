# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import *


def lagrange_interpolation(x, y, degree):
    n = degree + 1
    L = np.ones(6, dtype=np.float64)
    for i in range(n):
        for j in range(n):
            if j != i:
                L[0] = L[0] / (x[i] - x[j])
    L = L * y
    return L


def _lagrange(t, x0, L):
    n = len(L)
    for i in range(n):
        for j in range(n):
            if j != i:
                L[0] = L[0] * (t - x0[0])

    return np.sum(L)


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

    # l = lagrange_interpolation(x, y, 5)
    # _lagrange(t, x, l)

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.plot(x, y, color='m', linestyle='', marker='o', label='给定数据')
    plt.plot(t, c5, color='b', linestyle='-', marker='', label="拉格朗日插值曲线")
    plt.plot(t, c3, color='g', linestyle='-', marker='', label="三次样条插值曲线")
    plt.legend(loc='best')
    plt.show()
