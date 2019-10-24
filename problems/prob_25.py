import sys
sys.path.insert(0, '/Users/oisin-brogan/Code/project_euler/snippets')
from fib_n import fib_n

f_n_2 = 1
f_n_1 = 1
f_n = f_n_2 + f_n_1

num_digits = len(str(f_n))
i = 3
while num_digits < 1000:
    i += 1
    f_n_2 = f_n_1
    f_n_1 = f_n
    f_n = f_n_2 + f_n_1
    num_digits = len(str(f_n))

print(i, f_n, num_digits)
