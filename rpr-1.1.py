from copy import deepcopy
from numpy import *
import matplotlib as mpl
import matplotlib.pyplot as plt


def f(y, x):
    return [y[1], 2 * y[1] * y[1] * x / y[0]]


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
    print("y=%.5f t=%.5f" % (z, p))


a, b = 2, 2.8
h, hp = 0.025, 0.1
n = int(ceil((b - a) / h)) + 1
k = int(hp / h)
x = [i * h + a for i in range(n)]
y = [[2, 0.5]]
y = adams(n, runge(4, 2, y, x, h), x, h)
f = open('out.txt', mode='w')
print('t\t\ty\t\ty\'')
for i in range(0, n):
    print("%.4f" % (x[i]), end='\t')
    for j in range(len(y[i])):
        print("%.4f" % (y[i][j]), end='\t')
        f.write("%.4f\t" % (y[i][j]))
    print()
    f.write('\n')
z = 2.13867
Y = []
X = []
for i in range(n):
    if abs(y[i][0] - z) <= 0.1 and len:
        Y.append(y[i][0])
        X.append(x[i])
interpolation(len(Y), z, Y, X)

dpi = 200
fig = plt.figure(dpi=dpi, figsize=(1024 / dpi, 768 / dpi))
mpl.rcParams.update({'font.size': 10})

plt.axis([2, 2.8, 0, 3])

plt.title('')
plt.xlabel('t')
plt.ylabel('y,y\'')
y1 = [y[i][0] for i in range(n)]
y2 = [y[i][1] for i in range(n)]
plt.plot(x, y1, color='blue', linewidth=1,
         label='y(t)')
plt.plot(x, y2, color='red',  linewidth=1,
         label='y\'(t)')

plt.legend(loc='upper right')
fig.savefig('trigan.png')
