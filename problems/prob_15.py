import sys
n = int(sys.argv[1])

look_up_table = {(1, 1): 2}
x, y = 1, 1 #x is width, y is height

def num_ways(i, j):
    if i == 0 or j ==0:
            return 1

    if (i,j) in look_up_table:
        return look_up_table[(i,j)]
    if (j,i) in look_up_table:
        return look_up_table[(j,i)]

    return num_ways(i-1, j) + num_ways(i, j-1)

while (n, n) not in look_up_table:
    x += 1
    y = 0
    while y < x:
        y += 1
        look_up_table[(x, y)] = num_ways(x, y)

    if x > n or y > n:
        print('x = %d, y = %d'%(x, y))
        print('We missed %d, %d. Breaking'%(n,n))
        break

print(look_up_table[(n,n)])
