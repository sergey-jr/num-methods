from numpy import *


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
    print("y=%.6f t=%.6f" % (z, p))


x = [-4.5, -4.4, -4.3]
y = [8.7495, 9.4995, 10.2495]
z = 9.5
interpolation(len(x), z, y, x)
