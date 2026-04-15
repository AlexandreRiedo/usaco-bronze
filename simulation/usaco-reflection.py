grid_size, num_updates = map(int, input().split())
grid = []
for _ in range(grid_size):
    grid.append([char for char in input()])
updates = [
    tuple(item - 1 for item in map(int, input().split())) for _ in range(num_updates)
]


def calculate_reflective(grid, grid_size) -> int:
    operations_used = 0
    for x in range(grid_size // 2):
        for y in range(grid_size // 2):
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

            operations_used += min(count)
    return operations_used


def apply_update(grid, update) -> None:
    if grid[update[0]][update[1]] == "#":
        grid[update[0]][update[1]] = "."
    else:
        grid[update[0]][update[1]] = "#"


# Before any updates
print(calculate_reflective(grid, grid_size))

# After every update
for update in updates:
    apply_update(grid, update)
    print(calculate_reflective(grid, grid_size))
