import sys
sys.path.insert(0, '/Users/oisin-brogan/Code/project_euler/snippets')
from proper_divisors_sum import proper_divisors_sum

abundent_numbers = []
for n in range(1, 28123-12+1):
    if proper_divisors_sum(n) > n:
        abundent_numbers.append(n)

culprits = list(range(1, 24))

for candidate in range(24, 28123):
    s = {}
    for i in abundent_numbers:
        if i in s:
            #candidate can be constrcucted as sum of two
            break
        if (i > candidate - 12):
            #Won't find anything smaller
            culprits.append(candidate)
            break
        else:
            s[candidate - i] = i
            if i == candidate - i:
                break
#print(abundent_numbers[:100])
print(sum(culprits))
