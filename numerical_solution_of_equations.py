import math


class Iteration():
    def __init__(self):
        self.answer = 1.368808107
        self.x0 = 1
        self.iter = 30

    def iteration_1(self):
        x = self.x0
        x1 = self.x0
        for i in range(self.iter):
            x = 20 / (x * x + 2 * x + 10)
            print('step {0} is {1}'.format(str(i + 1), str(x)))
            if math.fabs(x - x1) <= 1e-9:
                break
            else:
                x1 = x
        print("the error {}".format(math.fabs(self.answer - x)))

    def iteration_2(self):
        x = self.x0
        x1 = self.x0
        for i in range(self.iter):
            x = (20 - 2 * x * x - x * x * x) / 10
            print('step {0} is {1}'.format(str(i + 1), str(x)))
            if math.fabs(x - x1) <= 1e-9:
                break
            else:
                x1 = x
        print("the error {}".format(math.fabs(self.answer - x)))

    def steffensen_1(self):
        x = self.x0
        x1 = self.x0
        for i in range(self.iter):
            y = 20 / (x * x + 2 * x + 10)
            z = 20 / (y * y + 2 * y + 10)
            if z - 2 * y + x == 0:
                break
            x = x - (y - x) * (y - x) / (z - 2 * y + x)
            print('step {0} is {1}'.format(str(i + 1), str(x)))
            if math.fabs(x - x1) <= 1e-9:
                break
            else:
                x1 = x
        print("the error {}".format(math.fabs(self.answer - x)))

    def steffensen_2(self):
        x = self.x0
        x1 = self.x0
        for i in range(self.iter):
            y = (20 - 2 * x * x - x * x * x) / 10
            z = (20 - 2 * y * y - y * y * y) / 10
            if z - 2 * y + x == 0:
                break
            x = x - (y - x) * (y - x) / (z - 2 * y + x)
            print('step {0} is {1}'.format(str(i + 1), str(x)))
            if math.fabs(x - x1) <= 1e-9:
                break
            else:
                x1 = x
        print("the error {}".format(math.fabs(self.answer - x)))

    def newton(self):
        x = self.x0
        x1 = self.x0
        for i in range(self.iter):
            x = x - (x * x * x + 2 * x * x + 10 * x - 20) / (3 * x * x + 4 * x + 10)
            print('step {0} is {1}'.format(str(i + 1), str(x)))
            if math.fabs(x - x1) <= 1e-9:
                break
            else:
                x1 = x
        print("the error {}".format(math.fabs(self.answer - x)))


if __name__ == '__main__':
    equation = Iteration()
    print('------------iteration_1--------------')
    equation.iteration_1()
    print('------------iteration_2--------------')
    equation.iteration_2()
    print('------------steffensen_1--------------')
    equation.steffensen_1()
    print('------------steffensen_2--------------')
    equation.steffensen_2()
    print('------------newton--------------')
    equation.newton()
