import sys
from functools import reduce
sys.path.insert(0, '/Users/oisin-brogan/Code/project_euler/snippets')
from prime_factors import prime_factors

n = int(sys.argv[1])

def merge_list(li, lj):
    new_list = []
    i, j = 0, 0
    while i < len(li) and j < len(lj):
        if li[i] < lj[j]:
            new_list.append(li[i])
            i += 1
        elif li[i] > lj[j]:
            new_list.append(lj[j])
            j += 1
        else: #i==j
            new_list.append(li[i])
            i += 1
            j += 1

    if i == len(li):
        new_list += lj[j:]
    else:
        new_list += li[i:]

    return new_list

factors = []

for i in range(2, n+1):
    candidates = prime_factors(i)
    factors = merge_list(factors, candidates)

print(reduce(lambda x, y: x*y, factors))
