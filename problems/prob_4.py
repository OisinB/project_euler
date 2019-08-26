def is_plaidrome(n):
  str_n = str(n)
  return str_n[::-1] == str_n

result = 0

for i in range(99,10,-1):
    for j in range(i,10, -1):
        if result/j > i:
            break #i*j < result, can't be biggest
        test = i*j
        if is_plaidrome(test):
            result = test #we only test i*j bigger than result, so we don't have to max

print(result)
