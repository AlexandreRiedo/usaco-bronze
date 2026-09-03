import itertools

for _ in range(int(input())):
    s = input()
    a_runs = []
    adjacent_b = 0

    for c, g in itertools.groupby(s):
        if c == "A":
            a_runs.append(len(list(g)))
        else:
            adjacent_b += min(len(list(g)), 2)

    if len(a_runs) <= adjacent_b:
        print(sum(a_runs))
    else:
        print(sum(a_runs) - min(a_runs))
