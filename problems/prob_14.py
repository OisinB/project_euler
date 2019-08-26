def collatz(i):
    if i%2 == 0:
        return i/2
    else:
        return 3*i + 1

collatz_ref = {1:1}

def collatz_len(i):
    if i in collatz_ref:
        return collatz_ref[i]
    else:
        return 1 + collatz_len(collatz(i))

max = 0
result = 0
for i in range(1, 1000000):
    canidate = collatz_len(i)
    if canidate > max:
        max = canidate
        result = i
    if i not in collatz_ref:
        collatz_ref[i] = canidate

print(result)
