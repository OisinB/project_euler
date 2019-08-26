import sys
sys.path.insert(0, '/Users/oisin-brogan/Code/project_euler/snippets')
from proper_divisors_sum import proper_divisors_sum

abundent_numbers = []
for n in range(1, 28123-12+1):
    if proper_divisors_sum(n) > n:
        abundent_numbers.append(n)

print(len(abundent_numbers))
print(abundent_numbers[:5])
