from math import sqrt

def prime_seive(n):
    primes = list(range(n+1))

    i = 2
    while i < sqrt(n):
        j = i*2
        while j <= n:
            primes[j] = 0
            j += i
        i += 1
        while primes[i] == 0 and i < sqrt(n):
            i += 1

    return sorted(list(set(primes))[2:])
