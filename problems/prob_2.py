import sys
sys.path.insert(0, '/Users/oisin-brogan/Code/project_euler/snippets')
from fib_n import fib_n

n = int(sys.argv[1])

i = 3
result = 0
fib = fib_n(i)

while fib < n:
    result += fib
    i += 3
    fib = fib_n(i)

print(result)
