with open('./inputs/input_22.txt') as f:
    names = f.readline()

names = names[1:-1].split('","')
names = sorted(names)

def alpha_value(str):
    #assumes a str of chars
    str = str.upper()
    return sum([ord(c)-64 for c in str])

print(alpha_value('COLIN'))

print(sum([alpha_value(name)*(i+1) for i, name in enumerate(names)]))
