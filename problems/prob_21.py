import sys
from itertools import combinations
from functools import reduce
sys.path.insert(0, '/Users/oisin-brogan/Code/project_euler/snippets')
from prime_factors import prime_factors

n = int(sys.argv[1])

#def proper_divisors(n):
#    pf = prime_factors(n)
#    divisors = [1]
#    for l in range(1, len(pf)):
#        divisors += [reduce(lambda x, y: x*y, combi) for combi in set(combinations(pf, l))]
#
#    return divisors

#Using https://mathschallenge.net/index.php?section=faq&ref=number/sum_of_divisors
def proper_divisors_sum(n):
    result = 1
    pf = prime_factors(n)
    pf_count = {}
    for f in pf:
        if f in pf_count:
            pf_count[f] += 1
        else:
            pf_count[f] = 1
    for factor, count in pf_count.items():
        result = result *(factor**(count+1) - 1)/(factor - 1)
    return result - n

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
