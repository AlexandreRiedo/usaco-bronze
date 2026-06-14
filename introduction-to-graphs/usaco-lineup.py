beside = {
    "Beatrice": [],
    "Belinda": [],
    "Bella": [],
    "Bessie": [],
    "Betsy": [],
    "Blue": [],
    "Buttercup": [],
    "Sue": [],
}

with open("lineup.in") as f:
    num_constraints = int(f.readline())

    for _ in range(num_constraints):
        phrase = f.readline().split()
        x, y = phrase[0], phrase[-1]
        beside[x].append(y)
        beside[y].append(x)

order = []

for cow, adj in sorted(beside.items()):
    adj = sorted(adj)

    if len(adj) == 0:
        order.append([cow]) if [cow] not in order else ""
    else:
        pass



from rich import print as rprint

rprint(f"{order=}")

with open("lineup.out", "w") as f:
    for item in order:
        f.write(f"{item}\n")
