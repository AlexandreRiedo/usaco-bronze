with open("factory.in") as f:
    num_stations = int(f.readline())
    graph = {i: [] for i in range(1, num_stations + 1)}

    for _ in range(num_stations - 1):
        a, b = map(int, f.readline().split())
        graph[a].append(b)

arrivals = set(graph.keys())
for start, adj in graph.items():
    wip = adj[:]
    visited = {start}

    while wip:
        curr = wip.pop()
        visited.add(curr)
        wip.extend([node for node in graph[curr] if node not in visited])

    arrivals = arrivals.intersection(visited)

with open("factory.out", "w") as f:
    if not arrivals:
        answer = "-1"
    else:
        answer = sorted(arrivals)[0]

    f.write(f"{answer}\n")
