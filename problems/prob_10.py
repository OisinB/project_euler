import sys
sys.path.insert(0, '/Users/oisin-brogan/Code/project_euler/snippets')
from sieve_of_eratosthenes import prime_seive

n = int(sys.argv[1])

primes = prime_seive(n)
print(sum(primes))
