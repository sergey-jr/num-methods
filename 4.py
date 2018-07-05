from copy import deepcopy
from numpy import *
import matplotlib as mpl
import matplotlib.pyplot as plt


def f(y, x):
    return [y[1], 3 * x + y[1] / x]


def plus(y, v):
    z = deepcopy(y)
    for i in range(len(y)):
        z[i] += v
    return z


def runge(n, m, y, x, h):
    Y = deepcopy(y)
    for i in range(n - 1):
        Y.append([0, 0])

    for i in range(n - 1):
        for j in range(m):
            k1 = f(Y[i], x[i])[j]
            k2 = f(plus(Y[i], h / 2 * k1), x[i] + h / 2)[j]
            k3 = f(plus(Y[i], h / 2 * k2), x[i] + h / 2)[j]
            k4 = f(plus(Y[i], h * k3), x[i] + h)[j]
            k = (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
            Y[i + 1][j] = Y[i][j] + k
    return Y


def adams(n, y, x, h):
    Y = y
    m = len(y)
    k = n - m
    for i in range(k):
        Y.append([0, 0])

    for i in range(m - 1, n - 1):
        t = []
        for j in range(len(Y[i])):
            t.append(Y[i][j] + (h / 24) * (55 * f(Y[i], x[i])[j] - 59 * f(Y[i - 1], x[i - 1])[j] +
                                           37 * f(Y[i - 2], x[i - 2])[j] - 9 * f(Y[i - 3], x[i - 3])[j]))
        for j in range(len(Y[i])):
            Y[i + 1][j] = Y[i][j] + (h / 24) * (
                    9 * f(t, x[i] + h)[j] + 19 * f(Y[i], x[i])[j] - 5 * f(Y[i - 1], x[i - 1])[j] +
                    f(Y[i - 2], x[i - 2])[j])
    return Y


def interpolation(n, z, y, x):
    d = zeros((n, n))
    for i in range(n):
        d[i][0] = x[i]

    for j in range(1, n):
        for i in range(j, n):
            d[i][j] = (d[i][j - 1] - d[j - 1][j - 1]) / (y[i] - y[j - 1])
    p = d[n - 1][n - 1]
    i = n - 2
    while i >= 0:
        p = p * (z - y[i]) + d[i][i];
        i -= 1
    return p


def krai(a, b, h, start, z, x):
    n = int(ceil((b - a) / h)) + 1
    res_x = []
    res_y = []
    for i in range(n):
        y = [[start, i * h + a]]
        y = adams(len(x), runge(4, 2, y, x, h), x, h)
        res_y.append(y[-1][0])
        res_x.append(i * h + a)
    return interpolation(len(res_x), z, res_y, res_x)


a, b = 1, 4
h, hp = 0.01, 0.1
n = int(ceil((b - a) / h)) + 1
k = int(hp / h)
x = [i * h + a for i in range(n)]
y1 = krai(a=-5, b=-4, h=h, start=2, z=9.5, x=x)
y = [[2, y1]]
y = adams(n, runge(4, 2, y, x, h), x, h)
print('t\t\ty\t\ty\'')
for i in range(0, n):
    print("%.4f" % (x[i]), end='\t')
    for j in range(len(y[i])):
        print("%.4f" % (y[i][j]), end='\t')
    print()
dpi = 200
y1 = [y[i][0] for i in range(n)]
y2 = [y[i][1] for i in range(n)]
fig = plt.figure(dpi=dpi, figsize=(1024 / dpi, 768 / dpi))
mpl.rcParams.update({'font.size': 10})

plt.axis([min(x) - 0.5, max(x) + 0.5, min(min(y1), min(y2)) - 0.5, max(max(y1), max(y2)) + 0.5])

plt.title('')
plt.xlabel('t')
plt.ylabel('y,y\'')
plt.plot(x, y1, color='blue', linewidth=1,
         label='y(t)')
plt.plot(x, y2, color='red', linewidth=1,
         label='y\'(t)')

plt.legend(loc='upper right')
fig.savefig('4.png')
