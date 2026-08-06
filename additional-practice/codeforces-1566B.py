from itertools import groupby

for _ in range(int(input())):
    s = input()

    if "0" not in s:
        base_score = 0
    elif int(s, 2) == 0:
        base_score = 1
    else:
        base_score = 2

    split_score = 0
    for key, group in groupby(s):
        if key == "0":
            split_score += 1

    print(min(base_score, split_score))
