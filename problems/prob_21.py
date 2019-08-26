import sys
from itertools import combinations
from functools import reduce
sys.path.insert(0, '/Users/oisin-brogan/Code/project_euler/snippets')
from proper_divisors_sum import proper_divisors_sum

n = int(sys.argv[1])

result = 0
look_up_table = {1:0}

for a in range(2, n+1):
    b = proper_divisors_sum(a)
    look_up_table[a] = b
    if b == a:
        pass
    if b < a and look_up_table[b] == a:
        result += (a + b)

print(result)
