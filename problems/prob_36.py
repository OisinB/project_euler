def is_palindrome(string):
    return string == string[::-1]

total = 0
for i in range(1, 10**6, 2):
    if is_palindrome(str(i)):
        bin_str = str(bin(i))[2:]
        if is_palindrome(bin_str):
            total += i

print(total)
