from collections import defaultdict

from rich import print as rprint


def find_next_idx(milking_order, start):
    for i in range(start, len(milking_order)):
        if milking_order[i] == -1:
            continue
        else:
            break
    else:
        return None

    return milking_order[i]


with open("milkorder.in") as file:
    num_cows, _, num_position = map(int, file.readline().split())
    cow_to_hierarchy = {
        cow: idx for idx, cow in enumerate(map(int, file.readline().split()), 1)
    }
    hierarchy_list = list(cow_to_hierarchy.keys())
    ordering = defaultdict(int)
    for _ in range(num_position):
        cow, order = map(int, file.readline().split())
        ordering[order] = cow

hierarchy_left_idx = 0

milking_order = [-1 for _ in range(num_cows)]
used_cows = set()
for order, cow in ordering.items():
    milking_order[order - 1] = cow
    used_cows.add(cow)

curr_hierarchy_idx = 0
curr_milking_idx = 0
while True:
    if milking_order[curr_milking_idx] != -1:
        curr_milking_idx += 1
        used_cows.add(milking_order[curr_milking_idx])
    else:
        next_idx = find_next_idx(milking_order, curr_milking_idx)
        if next_idx is None:
            break
        next_value = milking_order[next_idx]

        if next_value not in hierarchy_list:
            break


rprint(f"{num_cows=} {num_position=}")
rprint(f"{cow_to_hierarchy=}")
rprint(f"{hierarchy_list=}")
rprint(f"{ordering=}")
rprint(f"{milking_order=}")
rprint(f"{used_cows=}")
rprint(f"{curr_milking_idx=}")

"""
3 4 5 1
"""
