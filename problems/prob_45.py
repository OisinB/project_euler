from math import sqrt

found = False
n = 285
while not found:
  n += 1
  Tn = (n * (n+1))/2
  n_p = (1 + sqrt(1 + 24*Tn))/6
  if n_p.is_integer():
    n_h = (1 + sqrt(1 + 8*Tn))/4
    if n_h.is_integer():
        found = True

print(n, n_p, n_h, Tn)
