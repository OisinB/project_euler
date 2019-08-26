import sys
sys.path.insert(0, '/Users/oisin-brogan/Code/project_euler/snippets')
from prime_factors import prime_factors
from functools import reduce

n = int(sys.argv[1])

triangular_n = 3
i = 2

while True:
    pfs = prime_factors(triangular_n)

    count = {}
    for pf in pfs:
        if pf not in count:
            count[pf] = 1
        else:
            count[pf] += 1

    num_factors = 1
    for x in count.values():
        num_factors = num_factors * (x+1)

    if num_factors >= n:
        print(triangular_n)
        break

    i += 1
    triangular_n += i
