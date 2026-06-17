def solve():
    with open("family.in") as f:
        n, a, b = f.readline().split()
        mother = {}
        for _ in range(int(n)):
            parent, child = f.readline().split()
            mother[child] = parent

    def chain(x):
        path = [x]
        while path[-1] in mother:
            path.append(mother[path[-1]])
        return path

    # depth of each ancestor above b (b itself = 0)
    above_b = {node: depth for depth, node in enumerate(chain(b))}

    # first ancestor of a that is also an ancestor of b = LCA
    da = db = None
    for depth, node in enumerate(chain(a)):
        if node in above_b:
            da, db = depth, above_b[node]
            break

    def grandmother(d):
        return "mother" if d == 1 else "great-" * (d - 2) + "grand-mother"

    def aunt(d):
        return "great-" * (d - 2) + "aunt"

    if da is None:
        ans = "NOT RELATED"
    elif da == 0:  # a is an ancestor of b
        ans = f"{a} is the {grandmother(db)} of {b}"
    elif db == 0:  # b is an ancestor of a
        ans = f"{b} is the {grandmother(da)} of {a}"
    elif da == 1 and db == 1:
        ans = "SIBLINGS"
    elif da >= 2 and db >= 2:  # type: ignore
        ans = "COUSINS"
    elif da == 1:  # a is the shallower one -> a is the aunt
        ans = f"{a} is the {aunt(db)} of {b}"
    else:
        ans = f"{b} is the {aunt(da)} of {a}"

    with open("family.out", "w") as f:
        f.write(ans + "\n")


solve()
