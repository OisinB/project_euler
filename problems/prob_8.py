from functools import reduce

with open('./inputs/input_8.txt') as f:
    lines = f.readlines()

str = ''.join([l.strip() for l in lines])

result = 0
for i in range(len(str)-13):
    candidate = str[i:i+13]
    x = reduce(lambda x, y: x*y, [int(c) for c in candidate])
    result = max(result, x)

print(result)
