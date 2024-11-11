from scipy.integrate import nquad
from math import sqrt

def f(x, y, z):
    return (x+y+z) / (sqrt(2*x**2 + 4*y**2 + 5*z**2))



def zbounds(x, y):
    return [0, sqrt(1 - x**2 - y**2)]


def ybounds(x):
    return [0, sqrt(1 - x**2)]


def xbounds():
    return [0, 1]


I = nquad(f, [zbounds, ybounds, xbounds])

print(I[0])
