with open('./inputs/input_11.txt') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    lines[i] = [int(x) for x in l.split(' ')]

result = 0
A = len(lines)
for i in range(A):
    l = lines[i]
    B = len(l)
    for j in range(B - 3):
        #right
        result = max(l[j]*l[j+1]*l[j+2]*l[j+3], result)
        if i <= A - 4:
            #down
            result = max(l[j]*lines[i+1][j]*lines[i+2][j]*lines[i+3][j], result)
            #down right
            result = max(l[j]*lines[i+1][j+1]*lines[i+2][j+2]*lines[i+3][j+3], result)
        if i >= 3:
            #up right
            result = max(l[j]*lines[i-1][j+1]*lines[i-2][j+2]*lines[i-3][j+3], result)
print(result)
