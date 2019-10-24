max_length = 0
result = 0

for n in range(2, 1001):
    length = 0
    remainder = 1
    remainders = [remainder]

    while remainder > 0:
        remainder = remainder*10%n

        try:
            first_seen = remainders.index(remainder)
            length = len(remainders) - first_seen
            break
        except ValueError:
            remainders.append(remainder)

    if length > max_length:
        max_length = length
        result = n

print(result, max_length)
