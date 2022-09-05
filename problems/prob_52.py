def is_palindrome(a, b):
  li1 = [c for c in a]
  li2 = [c for c in b]
  li1.sort()
  li2.sort()

  return li1 == li2

found = False
i = 0
while not found:
  i += 1
  found = True
  for f in range(2, 7):
    b = i*f
    if not is_palindrome(str(i), str(b)):
      found = False
      break

print(i)
