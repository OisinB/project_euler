from math import factorial

factorials = {}
for i in range(10):
    factorials[str(i)] = factorial(i)

def sum_of_fractional_digits(n):
    total = 0
    str_n = str(n)

    for d in str_n:
        total += factorials[d]

    return(total)

total = 0

#max to search is to 10**7, as fact(9)*7 < 10**7
for i in range(10, 10**7):
    if i == sum_of_fractional_digits(i):
        total += i

print(total)
