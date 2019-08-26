with open('./inputs/input_67.txt') as f:
    triangle = f.readlines()

for i, l in enumerate(triangle):
    triangle[i] = [int(x) for x in l.split(' ')]

height = len(triangle) - 1
width = len(triangle[-1]) - 1

while height > 0:
    #go up a row
    height -= 1
    width -= 1
    for i in range(width+1):
        #merge the max of the options
        triangle[height][i] += max(triangle[height+1][i]
                , triangle[height+1][i+1])

print(triangle[0][0])
