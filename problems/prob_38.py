from itertools import permutations

li = permutations('123456789')
candidates = [''.join(i) for i in li]
candidates.sort(reverse=True)

def test(n):
    for l in range(1, 6):
        cur = l
        prod = 2
        x = int(n[:l])

        while cur < 9:
            next = str(x*prod)
            if next != n[cur:cur+len(next)]:
                break

            cur += len(next)
            prod += 1

            if cur == 9:
                return True

    return False

for i in candidates:
    if test(i):
        print(i)
        break
