import sys

n = int(sys.argv[1])

s = sum(range(n+1))
result = sum([i*(s-i) for i in range(n+1)])

print(result)
