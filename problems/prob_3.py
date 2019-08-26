import sys
sys.path.insert(0, '/Users/oisin-brogan/Code/project_euler/snippets')
from prime_factors import prime_factors

n = int(sys.argv[1])

print(prime_factors(n)[-1])
