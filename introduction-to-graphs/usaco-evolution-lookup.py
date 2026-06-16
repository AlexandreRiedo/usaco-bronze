import itertools
from collections import defaultdict

with open("evolution.in") as f:
    num_sub = int(f.readline())
    chars = defaultdict(set)

    for idx in range(num_sub):
        _, *sub_chars = f.readline().split()
        for char in sub_chars:
            chars[char].add(idx)

with open("evolution.out", "w") as f:
    for a, b in itertools.combinations(chars.values(), 2):
        if a & b and not (a.issubset(b) or b.issubset(a)):
            f.write("no\n")
            break
    else:
        f.write("yes\n")
