with open("evolution.in") as f:
    num_sub = int(f.readline())
    subs = []
    chars = set()

    for _ in range(num_sub):
        _, *sub_chars = f.readline().split()
        if sub_chars:
            subs.append(set(sub_chars))
            chars.update(sub_chars)

graph = [set() for _ in range(len(subs))]

for at_idx, at in enumerate(subs):
    for to_idx, to in enumerate(subs):
        if at_idx == to_idx:
            continue

        if at & to:
            graph[at_idx].add(to_idx)
            graph[to_idx].add(at_idx)

with open("evolution.out", "w") as f:
    if any(len(adj) > 1 for adj in graph):
        f.write("no\n")
    else:
        f.write("yes\n")
