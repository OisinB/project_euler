#p = a + b + c
#
#a^2 + b^2 = c^2
#a <= b <= c
#
#p = a + b + sqrt(a^2 + b^2)
#sqrt(a^2 + b^2) = p - a - b
#a^2 + b^2 = (p-a-b)(p-a-b)
#a^2 + b^2 = p^2-ap-bp-ap+a^2+ab-bp+ab+b^2
#p^2-2ap-2bp+2ab = 0
#b(2a-2p) = -p^2 + 2ap
#b = (-p^2 + 2ap)/(2a-2p)
#b = (p^2 - 2ap)/(2p-2a)

max = 0
result = 0
for p in range(1, 1001):
    soluntions = 0
    for a in range(1, int(p/3)):
        b = (p*p - 2*a*p)/(2*p-2*a)

        if b.is_integer():
            soluntions+=1

    if soluntions > max:
        max = soluntions
        result = p

print(result)
