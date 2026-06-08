N = int(input())
order = list(input())

flips = 0

for i in range(N - 2, -1, -2):
    pair = "".join(order[i : i + 2])

    if (pair == "HG" and flips % 2 == 1) or (pair == "GH" and flips % 2 == 0):
        flips += 1

print(flips)
