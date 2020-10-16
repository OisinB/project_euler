def s(n):
    operand = ''
    while n > 9:
        operand = '9' + operand
        n -= 9

    operand = str(n) + operand

    return int(operand)

def big_s(n):
    total = 0
    for i in range(1, n+1):
        total += s(i)
    return total

print(big_s(20))
print(s(1000))

from math import sqrt
phi = (sqrt(5) + 1)/2

def fib_n(n):
    return int((pow(phi, n) - pow(-phi, -n))/sqrt(5))

print(big_s(fib_n(90)))%1000000007
