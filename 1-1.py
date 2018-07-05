from math import *


def find(a: float, b: float, h: float):
    y = [0]
    x = [a]
    i = 0
    while True:
        s = 1 / h - sqrt(1 / (h ** 2) - (y[i] ** 2 + 2 + (2 * y[i]) / h))
        y.append(int(s*10000.0)/10000.0)
        x.append(int((x[i] + h)*100)/100.0)
        if i == int((b-a)/h)-1:
            break
        i += 1
    for i in range(len(y)):
        print('{}\t{}'.format(x[i], y[i]))


find(0, 1, 0.1)
