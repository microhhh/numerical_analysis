# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def polyfit(x, y, degree):
    n = degree + 1
    A = np.zeros((n, n), dtype=np.float64)
    b = np.zeros((n, 1), dtype=np.float64)
    for i in range(n):
        for j in range(n):
            A[i, j] = np.sum(np.power(x, i) * np.power(x, j))

    for i in range(n):
        b[i] = np.sum(np.power(x, i) * y)
    a = np.linalg.solve(A, b)
    print(A)
    print(b)
    return a


if __name__ == '__main__':
    x = np.array([0.0, 0.1, 0.2, 0.3, 0.5, 0.8, 1.0], dtype=np.float64)
    y = np.array([1.0, 0.41, 0.50, 0.61, 0.91, 2.02, 2.46], dtype=np.float64)
    f3 = np.polyfit(x, y, 3)
    f4 = np.polyfit(x, y, 4)
    p3 = np.poly1d(f3)
    p4 = np.poly1d(f4)

    # z = polyfit(x, y, 3)

    print(p3)
    print(p4)

    t = np.linspace(0, 1.2, 1000)
    c3 = p3(t)
    c4 = p4(t)

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.plot(x, y, color='m', linestyle='', marker='o', label='给定数据')
    plt.plot(t, c3, color='b', linestyle='-', marker='', label="三次拟合曲线")
    plt.plot(t, c4, color='g', linestyle='-', marker='', label="四次拟合曲线")
    plt.legend(loc='best')
    plt.show()
