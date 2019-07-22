import sys
from math import sqrt

n = int(sys.argv[1])

phi = (sqrt(5) + 1)/2

def fib_n(n):
    return round((pow(phi, n) - pow(-phi, -n))/sqrt(5))

i = 3
result = 0
fib = fib_n(i)

while fib < n:
    result += fib
    i += 3
    fib = fib_n(i)

print(result)
