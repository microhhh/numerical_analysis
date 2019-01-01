# -*- coding: UTF-8 -*-
from math import sin


class GuassLegendre:
    def __init__(self):
        self.coef4 = {0.9061798459: 0.2369268851, 0.5384693101: 0.4786286705, 0: 0.5688888889}

    def compute(self, a, b, f):
        sum = 0.0
        for x, A in self.coef4.items():
            if x > 0:
                sum += A * f((a + b) / 2 + (b - a) * x / 2)
                sum += A * f((a + b) / 2 + (b - a) * (-x) / 2)
            else:
                sum += A * f((a + b) / 2 + (b - a) * x / 2)
        sum = sum * (b - a) / 2
        return sum

    def integration(self, seg, a, b, f):
        sub = [a + i * (b - a) / seg for i in range(seg + 1)]
        sum = 0.0
        for i in range(seg):
            t = self.compute(sub[i], sub[i + 1], f)
            sum += t
            print('The {0} segmentation integration: {1}'.format(i + 1, t))
        return sum


def f(x):
    y = (10 / x) * (10 / x) * sin(10 / x)
    return y


if __name__ == '__main__':
    n = 4
    segment = 10
    a = 1
    b = 3
    x = 0
    equation = GuassLegendre()
    result = equation.integration(segment, a, b, f)
    print('result={}'.format(result))
