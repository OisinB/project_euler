import sys

n = int(sys.argv[1])

for a in range(1, n-1):
    b = (n**2 - 2*n*a)/(2*n - 2*a)
    if b%1 != 0 or b < 0:
        continue
    c = n - a - b
    if a**2 + b**2 == c**2:
        print(a, b, c, a*b*c)
        break
