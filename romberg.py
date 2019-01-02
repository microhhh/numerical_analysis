# -*- coding: UTF-8 -*-
import numpy as np
from math import sin


class Romberg:
    def __init__(self, a, b, d, f):
        self.a = a
        self.b = b
        self.f = f
        self.T = np.zeros((d, d), dtype=np.float64)

    def trapezoid(self, h, j):
        integration = f(self.a) + f(self.b)
        n = pow(2, j)
        for k in range(1, n):
            integration += 2 * f(a + k * h)
        integration *= (h / 2)
        return integration

    def compute(self, d):
        for j in range(d):
            self.T[j, 0] = self.trapezoid((b - a) / pow(2, j), j)
        for j in range(d):
            for k in range(1, j + 1):
                self.T[j, k] = (pow(4, k) * self.T[j, k - 1] - self.T[j - 1, k - 1]) / (pow(4, k) - 1)

        return self.T


def f(x):
    y = (10 / x) * (10 / x) * sin(10 / x)
    return y


if __name__ == '__main__':
    a = 1
    b = 3
    d = 8
    equation = Romberg(a, b, d, f)
    result = equation.compute(d)
    print(result)
