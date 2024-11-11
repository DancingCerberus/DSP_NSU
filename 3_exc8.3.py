from matplotlib import pyplot as plt
from scipy.integrate import nquad


def A(x):
    return 2 if 0 < x < 1 else 0



def xbounds():
    return [0, 1]



I = nquad(A, [xbounds])

x_values = []
y_values = []
x = -6
for i in range(0, 1200):
    x_values.append(x)
    y_values.append(A(x))
    x += 0.01

plt.plot(x_values, y_values)
plt.axis((-2, 3, -0.25, 2.25))
plt.show()


print(I)