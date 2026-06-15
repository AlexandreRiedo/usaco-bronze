from math import inf


def explore(start_idx, positions):
    visited = set()
    todo = [start_idx]

    while todo:
        curr_idx = todo.pop()

        left = positions[curr_idx - 1] if curr_idx > 0 else inf
        curr = positions[curr_idx]
        right = positions[curr_idx + 1] if curr_idx < len(positions) - 1 else inf

        if curr in visited:
            continue
        else:
            visited.add(curr)

            if abs(curr - left) < abs(curr - right):
                todo.append(curr_idx - 1)
            elif abs(curr - left) > abs(curr - right):
                todo.append(curr_idx + 1)
            else:
                todo.append(curr_idx - 1)

    return visited


with open("hoofball.in") as f:
    num_cows = int(f.readline())
    positions = list(sorted(map(int, f.readline().split())))

explorations = []

for idx, pos in enumerate(positions):
    explorations.append(explore(idx, positions))
explorations.sort(key=lambda x: len(x), reverse=True)

ignore = [False for _ in range(len(explorations))]
count = 0

for parent_idx, parent_exploration in enumerate(explorations):
    if ignore[parent_idx]:
        continue
    ignore[parent_idx] = True

    for child_idx, child_exploration in enumerate(explorations):
        if len(child_exploration) > len(parent_exploration) or ignore[child_idx]:
            continue
        if child_exploration.issubset(parent_exploration):
            ignore[child_idx] = True

    count += 1

with open("hoofball.out", "w") as f:
    f.write(f"{count}\n")
