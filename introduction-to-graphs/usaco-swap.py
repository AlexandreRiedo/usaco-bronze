with open("swap.in") as f:
    num_cows, num_repeats = map(int, f.readline().split())
    a1, a2 = map(lambda x: int(x) - 1, f.readline().split())
    b1, b2 = map(lambda x: int(x) - 1, f.readline().split())

order = list(range(1, num_cows + 1))

for _ in range(num_repeats):
    order[a1 : a2 + 1] = order[a2 : a1 - 1 : -1]
    order[b1 : b2 + 1] = order[b2 : b1 - 1 : -1]

with open("swap.out", "w") as f:
    for item in order:
        f.write(f"{item}\n")


"""
1234567

1543267
1576234
"""
