from math import factorial, pi
from matplotlib import pyplot as plt
k = int(input())


def sin(x):
    res = 0
    for i in range(0, k):
        res += (-1)**i * (x ** (2 * i + 1)) / factorial((2 * i + 1))
    return res


x = 0
x_values = []
y_values = []
for i in range(0, 120):
    x_values.append(x)
    y_values.append(sin(x))
    x += 0.1


plt.plot(x_values, y_values)
plt.axis((0, 6.28, -1, 1))
plt.show()
