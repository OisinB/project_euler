import sys
sys.path.insert(0, '/Users/oisin-brogan/Code/project_euler/snippets')
from sieve_of_eratosthenes import prime_seive

#You can get the same result by setting n = x-c in n**2 -n + 41
#, finding c to maximise b while keeping it prime and less 1000

primes = prime_seive(10000)

def count_primes(a, b):
    length = 0
    i = 0
    poly = i*i + a*i + b
    while poly in primes:
        length += 1
        i += 1
        poly = i*i + a*i + b

    return length

max_length = 0
result = ()

for a in range(-999, 1000):
    for b in range(1001):
        length = count_primes(a, b)
        if length > max_length:
            max_length = length
            result = (a, b)
    if a%100 == 0:
        print(a)

print(result)
