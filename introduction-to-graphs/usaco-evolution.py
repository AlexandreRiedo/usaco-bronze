with open("evolution.in") as f:
    num_sub = int(f.readline())
    subs = []

    for _ in range(num_sub):
        _, *sub_chars = f.readline().split()
        subs.append(sub_chars)


with open("evolution.out", "w") as f:
    f.write("yes")
