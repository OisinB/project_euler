from math import sqrt, floor, ceil

with open('/Users/oisin.brogan/Code/project_euler/inputs/input_42.txt') as f:
    words = f.read()

words = words.split('","')
words[0] = words[0].strip('"')
words[-1] = words[-1].strip('"')

def ord_sum(string):
    return sum([ord(c)-64 for c in string])

def is_triangle(n):
    square = n*2
    root = sqrt(square)
    base = floor(root)
    height = ceil(root)
    if base == height:
        return False
    else:
        return square == floor(root)*ceil(root)

count = 0
for word in words:
    if is_triangle(ord_sum(word)):
        count += 1

print(count)
