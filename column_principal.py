# -*- coding: UTF-8 -*-
import numpy as np

class GaussElimination:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.n = self.a.shape[0]
        print('-------init matrix-------')
        print("A=")
        print(self.a)
        print("b=")
        print(self.b)
        print("det A=")
        print(np.linalg.det(a))
        # x = np.linalg.solve(a, b)


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

    def solve(self):
        n = self.n
        max_i = 0  # line num of max value
        max_v = m = self.a[0][0]
        for j in range(0, n - 1):
            for i in range(j, n):
                max_i, max_v = self.max(max_i, max_v, i, j)
            if max_v == 0:
                raise ValueError('no unique solution')
            if debug:
                print('max_v = %f' % max_v)
                print('max_i = %f , j = %f' % (max_i, j))
            if max_i != j:
                # jiaohuan ai hang he ajhang
                self.swap(max_i, j)
            if debug:
                print('SWAP*******')
                print(self.a)
                print(self.b)
            for p in range(j + 1, n):
                l = a[p][j] / a[j][j]
                # print('l = %f' % (l))
                b[p] -= l * b[j]
                for q in range(j, n):
                    a[p][q] -= l * a[j][q]
            if debug:
                print('CAL_a******')
                print(self.a)
                print(self.b)
            max_v = m
        if debug:
            print("************************")
            print(self.a)
            print(self.b)
        self.calculate()

    def calculate(self):
        n = self.n - 1
        xn = b[n] / a[n][n]
        print('xn = %f' % xn)


if __name__ == '__main__':
    debug = True

    # problem1
    a = np.array([[3.01, 6.03, 1.99],
                  [1.27, 4.16, -1.23],
                  [0.987, -4.81, 9.34]])
    print(a.shape)
    b = np.array([1, 1, 1])

    # problem2
    # a = np.array([[3.00, 6.03, 1.99],
    #               [1.27, 4.16, -1.23],
    #               [0.990, -4.81, 9.34]])
    # b = [1, 1, 1]

    equation = GaussElimination(a, b)
    # equation.solve()
