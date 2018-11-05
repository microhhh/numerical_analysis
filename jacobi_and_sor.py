import numpy as np


class Iteration:
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
        # print(np.linalg.solve(a, b))

    def jacobi(self, x, eps):
        L = np.tril(self.a, k=-1)
        U = np.triu(self.a, k=1)
        D = np.diag(np.diag(self.a))

        print('--------Jacobi--------')
        i = 1
        # print(np.linalg.norm(x, ord=np.inf))
        while np.linalg.norm(x, ord=np.inf) >= eps:
            # x=D^(-1)*[(L+U)x+b]
            x = np.dot(np.linalg.inv(D), b - np.dot((L + U), x))
            print('step {} in Jacobi'.format(i))
            i += 1
            print(x)

    def sor(self, x, w, eps):
        L = np.tril(self.a, k=-1)
        U = np.triu(self.a, k=1)
        D = np.diag(np.diag(self.a))

        i = 1
        print('--------SOR with w :{}-----'.format(w))
        while np.linalg.norm(x, ord=np.inf) >= eps:
            # x=(D-wL)^(-1)*{[(1-w)D+wU]x+wb}
            x = np.dot(np.linalg.inv(D + w * L), np.dot(((1 - w) * D - w * U), x) + w * b)
            print('step {} in SOR'.format(i))
            i += 1
            print(x)


if __name__ == '__main__':

    n = 10
    eps = 1e-6
    a = np.zeros((n, n), dtype=np.float64)
    b = np.zeros((n, 1), dtype=np.float64)
    x = np.ones((n, 1), dtype=np.float64)

    for i in range(n):
        a[i, i] = 20
    for i in range(n - 1):
        a[i, i + 1] = -8
        a[i + 1, i] = -8
    for i in range(n - 2):
        a[i, i + 2] = 1
        a[i + 2, i] = 1

    equation = Iteration(a, b)
    # equation.info()
    # equation.jacobi(x, eps)
    for w in [1.0, 1.2, 1.4, 1.6, 1.8]:
        equation.sor(x, w, eps)
    # equation.info()
    # equation.solve()
