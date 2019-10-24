import sys
sys.path.insert(0, '/Users/oisin-brogan/Code/project_euler/snippets')
from prime_factors import prime_factors

results = set()

for a in range(2, 101):
    for b in range(2, 101):
        results.add(a**b)

print(len(results))
