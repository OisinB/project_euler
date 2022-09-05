def self_power(n):
  return n**n

total = 0
for i in range(1, 1001):
  total += self_power(i)

print(total%(10**10))
