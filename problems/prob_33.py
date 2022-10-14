from functools import reduce

results = []

for b in range(10):
    for c in range(b+1,10):
        a = 9*b*c/(10*c - b)
        if a % 1 == 0 and a <10 and a > 0: #is an int
            #results.append(str(10*a + b) + '/' + str(10*c + a))
            results.append((10*a + b)/(10*c + a))
        a = 9*b*c/(10*b - c)
        if a % 1 == 0 and a <10 and a > 0: #is an int
            #results.append(str(10*b + a) + '/' + str(10*a + c))
            results.append((10*b + a)/(10*a + c))

result = reduce((lambda x, y: x * y), results)
print(result)
