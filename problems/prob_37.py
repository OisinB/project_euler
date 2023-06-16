import sys
sys.path.insert(0, '/Users/oisin.brogan/Code/project_euler/snippets')
from sieve_of_eratosthenes import prime_seive

primes = prime_seive(10**6)

allowed_final_digits = [3, 7]
allowed_starting_digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

truncatable_primes = []

#inital_pass
for n in allowed_starting_digits:
  for m in allowed_final_digits:
    candidate = n*10 + m
    if candidate in primes:
      truncatable_primes.append(candidate)

check = True
pow = 2

while True:
    check = False
    last_batch = [n for n in truncatable_primes if n > 10**(pow-1)]

    for n in allowed_starting_digits:
        for p in last_batch:
            candidate = n*(10**pow) + p
            if candidate in primes:
              truncatable_primes.append(candidate)
              check = True #found a new answer

    if not check:
        break
    pow += 1

def right_trun_test(n):
    while n:
        if n not in primes:
            return False
        n = int(n/10)
    return True

print([n for n in truncatable_primes if right_trun_test(n)])
