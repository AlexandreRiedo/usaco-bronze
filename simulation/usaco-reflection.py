grid_size, num_updates = map(int, input().split())
grid = []
for _ in range(grid_size):
    grid.append([char for char in input()])
updates = [
    tuple(item - 1 for item in map(int, input().split())) for _ in range(num_updates)
]


def calculate_reflective(grid, grid_size) -> int:
    operations_used = 0
    half_size = grid_size // 2
    for x in range(half_size):
        opp_x = grid_size - x - 1
        for y in range(half_size):
            opp_y = grid_size - y - 1
            
            dots = 0
            
            # Direct lookups avoid tuple allocation and for-loop overhead
            if grid[x][y] == ".": dots += 1
            if grid[opp_x][y] == ".": dots += 1
            if grid[x][opp_y] == ".": dots += 1
            if grid[opp_x][opp_y] == ".": dots += 1
            
            # The minimum operations required is the lesser of the dots 
            # count or the hashes count (4 - dots).
            operations_used += dots if dots < 2 else 4 - dots

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
