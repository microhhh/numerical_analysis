# -*- coding: UTF-8 -*-
import numpy as np

class GaussElimination:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.n = self.a.shape[0]
        self.x = np.ones(self.n, dtype=np.float64)

    def info(self):
        print("A=")
        print(self.a)
        print("b=")
        print(self.b)
        print("det A=")
        print(np.linalg.det(a))
        print("cond 1 A=")
        print(np.linalg.cond(a, p=1))
        print("cond 2 A=")
        print(np.linalg.cond(a, p=2))
        print("cond inf A=")
        print(np.linalg.cond(a, p=np.inf))
        # print(np.linalg.solve(a, b))

    def max(self, max_i, max_v, i, j):
        # get the max element
        a = self.a
        abs_a = abs(a[i][j])
        if max_v < abs_a:
            max_v = abs_a
            max_i = i
        return max_i, max_v

    def swap(self, i, j):  # change line
        self.a[[i, j], :] = self.a[[j, i], :]
        temp = self.b[i]
        self.b[i] = self.b[j]
        self.b[j] = temp

    def solve(self):
        n = self.n
        max_i = 0  # line index of max value
        max_v = m = self.a[0][0]
        for j in range(0, n - 1):
            for i in range(j, n):
                max_i, max_v = self.max(max_i, max_v, i, j)
            if max_v == 0:
                raise ValueError('no unique solution')
            if max_i != j:
                # swap two lines
                self.swap(max_i, j)
            for p in range(j + 1, n):
                coef = a[p][j] / a[j][j]
                b[p] = (b[p] - coef * b[j])
                for q in range(j, n):
                    a[p][q] -= coef * a[j][q]
            max_v = m
        self.calculate()
        print("x =")
        print(self.x)
        return self.x

    def calculate(self):
        n = self.n - 1
        i = n
        while i >= 0:
            line_sum = 0
            j = i + 1
            while j <= n:
                line_sum += a[i][j] * self.x[j]
                j = j + 1
            self.x[i] = (b[i] - line_sum) / a[i][i]
            i = i - 1
        return self.x

    def line_balance(self):
        # line balance method
        D = np.zeros([self.n, self.n], dtype=np.float64)
        line_max = a.max(axis=1)
        for i in range(0, self.n):
            D[i][i] = 1 / line_max[i]
        print("D=")
        print(D)
        self.a = np.dot(D, a)
        self.b = np.dot(D, b)

if __name__ == '__main__':

    # problem1
    a = np.array([[3.01, 6.03, 1.99],
                  [1.27, 4.16, -1.23],
                  [0.987, -4.81, 9.34]])
    b = np.array([1, 1, 1], dtype=np.float64)

    # problem2
    # a = np.array([[3.00, 6.03, 1.99],
    #               [1.27, 4.16, -1.23],
    #               [0.990, -4.81, 9.34]])
    # b = np.array([1, 1, 1], dtype=np.float64)

    equation = GaussElimination(a, b)
    equation.info()
    # equation.line_balance()
    # equation.info()
    equation.solve()
