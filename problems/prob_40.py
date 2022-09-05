construct = ''

i = 1
while len(construct) < 10**6:
    construct += str(i)
    i += 1

print(construct[11])
print(int(construct[0])*int(construct[9])*int(construct[99])*int(construct[999])*int(construct[9999])*int(construct[99999])*int(construct[999999]))
