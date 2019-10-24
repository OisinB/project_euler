import sys

def sum_of_power_digits(n, power):
    return sum([int(c)**power for c in str(n).zfill(power)])

power = int(sys.argv[1])
result = 0

for i in range(10, 10**(power+1)):
    if i == sum_of_power_digits(i, power):
        result += i

print(result)
