from rich import print as rprint

with open("milkorder.in") as file:
    num_cows, num_hierarchy, num_position = map(int, file.readline().strip().split())
    hierarchy = [
        int(num) for num in reversed(file.readline().strip().split())
    ]  # highest priorty at [-1]
    ordering = []
    for _ in range(num_position):
        cow, order = map(int, file.readline().strip().split())
        ordering.append((cow, order - 1))
    ordering.sort(key=lambda x: x[1], reverse=True)  # highest priority at [-1]


# def solve(hierarchy, ordering, num_cows):
used_ordering_idx = {order for cow, order in ordering}
for sick_idx in range(num_cows):
    # Setup
    milking = [-1 for _ in range(num_cows)]
    for cow, order in ordering:
        milking[order] = cow

    # Skip the idx used by the ordering cows
    if sick_idx in used_ordering_idx:
        continue
    

    rprint(f"{sick_idx=}")


rprint(f"{milking=}")

# with open("milkorder.out", "w") as f:
#     f.write(f"{solve(hierarchy, ordering, num_cows)}\n")

"""
3 4 5 1
-> 4 is the answer
"""
