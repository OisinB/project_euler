from itertools import permutations
perm = permutations('0123456789')

print(''.join(list(perm)[1000000-1]))
