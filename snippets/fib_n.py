from math import sqrt
phi = (sqrt(5) + 1)/2

def fib_n(n):
    return (pow(phi, n) - pow(-phi, -n))/sqrt(5)
