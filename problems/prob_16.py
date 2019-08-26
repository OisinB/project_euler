import sys
n = int(sys.argv[1])

#Easy solution
print(sum([int(c) for c in str(2**n)]))
