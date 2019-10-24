look_up_table = [[], [{1:1, 2:0, 5:0, 10:0, 20:0, 50:0, 100:0, 200:0}]]

coins = [200, 100, 50, 20, 10, 5, 2, 1]


def num_ways(n, c):
    ways = []

    if len(look_up_table) > n:
        for way in look_up_table[n]:
            way[c] += 1

    for c in coins:
        if n >= c:
            ways.append(num_ways(n-c, c))

    return total

for i in range(1, 21):
    look_up_table[i] = num_ways(i, coins)

for k, v in look_up_table.items():
    print(k, v)
