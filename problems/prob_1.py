from functools import reduce
import sys

n = int(sys.argv[1])

print(reduce(lambda x, y: x if (y%3!=0 and y%5!=0) else x+y, range(n)))
