from itertools import permutations

candidates = set([''.join(p) for p in permutations('123456789')])

results = []
for candidate in candidates:
    for i in range(1, 8):
        for j in range(i+1, 8):
            multiplicand = int(candidate[:i])
            multiplier = int(candidate[i:j])
            product = int(candidate[j:])

            if multiplicand*multiplier == product:
                if product not in results:
                    results.append(product)

print(sum(results))
