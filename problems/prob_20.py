import sys
from math import factorial
n = int(sys.argv[1])

#Easy solution
print(sum([int(c) for c in str(factorial(n))]))
