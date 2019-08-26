with open('./inputs/input_13.txt') as f:
    numbers = f.readlines()

numbers = [int(n[:12]) for n in numbers]

print(str(sum(numbers))[:10])
