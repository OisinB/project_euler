import sys
sys.path.insert(0, '/Users/oisin.brogan/Code/project_euler/snippets')
from sieve_of_eratosthenes import prime_seive

primes = prime_seive(10**6)

def check(str_n):
    for c in str_n:
        if int(str_n) not in primes:
            return False
        str_n = str_n[-1] + str_n[:-1]

    return True

ineligable = ['2', '4', '5', '6', '8', '0']

count = 0
for i in range(10**6):
    str_i = str(i)
    if i > 10 and any(word in str_i for word in ineligable):
        continue
    if check(str_i):
        count += 1

print(count)
