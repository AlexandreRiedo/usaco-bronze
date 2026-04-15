grid_size, num_updates = map(int, input().split())
grid = []
for _ in range(grid_size):
    grid.append([char for char in input()])
updates = [
    tuple(item - 1 for item in map(int, input().split())) for _ in range(num_updates)
]


def calculate_reflective_operations(grid, grid_size):
    operations_used = set()
    for y in range(grid_size // 2):
        for x in range(grid_size // 2):
            count = [0, 0]
            positions = [
                (x, y),
                (grid_size - x - 1, y),
                (x, grid_size - y - 1),
                (grid_size - x - 1, grid_size - y - 1),
            ]

            for pos in positions:
                if grid[pos[0]][pos[1]] == ".":
                    count[0] += 1
                else:
                    count[1] += 1

            if count.index(min(count)) == 0:
                for pos in positions:
                    if grid[pos[0]][pos[1]] == ".":
                        operations_used.add((pos[0], pos[1]))
            elif count.index(min(count)) == 1:
                for pos in positions:
                    if grid[pos[0]][pos[1]] == "#":
                        operations_used.add((pos[0], pos[1]))
    return operations_used


def apply_update(grid, update) -> None:
    if grid[update[0]][update[1]] == "#":
        grid[update[0]][update[1]] = "."
    else:
        grid[update[0]][update[1]] = "#"


### TESTING
# print(calculate_reflective_operations(grid, grid_size))

# Before any updates
ref_ops = calculate_reflective_operations(grid, grid_size)
curr_best = len(ref_ops)
print(curr_best)

# After every update
for update in updates:
    apply_update(grid, update)

    if update in ref_ops:
        ref_ops.remove(update)
    else:
        if len(ref_ops) == curr_best:
            new_ops = calculate_reflective_operations(grid, grid_size)
            if len(new_ops) < len(ref_ops):
                ref_ops = new_ops
        else:
            curr_best += 1
            ref_ops.add(update)
    print(len(ref_ops))


"""
4 5
..#.
##.#
####
..##
1 3
2 3
4 3
4 4
4 4
"""

"""
4 5
....
##.#
####
..##
0 2
1 2
3 2
3 3
3 3
"""
