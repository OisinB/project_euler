import sys
from math import factorial
n = int(sys.argv[1])

total = 1
previous = 1

for ring in range(1,(n+1)//2):
    for corner in range(4):
        total = total + previous + ring*2
        previous = previous + ring*2

print(total)
