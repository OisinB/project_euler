from prime_factors import prime_factors

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
