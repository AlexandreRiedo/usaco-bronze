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
            if grid[x][y] == ".":
                dots += 1
            if grid[opp_x][y] == ".":
                dots += 1
            if grid[x][opp_y] == ".":
                dots += 1
            if grid[opp_x][opp_y] == ".":
                dots += 1

            # The minimum operations required is the lesser of the dots
            # count or the hashes count (4 - dots).
            operations_used += dots if dots < 2 else 4 - dots

    return operations_used


def calculate_update_post(grid, update, grid_size) -> int:
    x = update[0]
    y = update[1]
    opp_x = grid_size - x - 1
    opp_y = grid_size - y - 1

    dots = 0

    if grid[x][y] == ".":
        dots += 1
    if grid[opp_x][y] == ".":
        dots += 1
    if grid[x][opp_y] == ".":
        dots += 1
    if grid[opp_x][opp_y] == ".":
        dots += 1

    hashes = 4 - dots

    if dots == 4 or hashes == 4:
        return -1
    if dots == 3 or hashes == 3:
        return 1
    elif dots == 2 or hashes == 2:
        return 2
    elif dots == 1 or hashes == 1:
        return 1

    return 9999999999999 # Fly Catcher



def apply_update(grid, update):
    if grid[update[0]][update[1]] == "#":
        grid[update[0]][update[1]] = "."
    else:
        grid[update[0]][update[1]] = "#"
    

# Before any updates
total = calculate_reflective(grid, grid_size)
print(total)

# After every update
original_grid = grid.copy()
for update in updates:
    apply_update(grid, update)
    total += calculate_update_post(grid, update, grid_size)
    print(total)

"""
TARGET
####
##.#
####
####

TARGET WITH OTHER CASES
####
##.#
#.##
####

####
#..#
#.##
####

####
#..#
#..#
####

EQUIVALENTS
####
#.##
####
####

####
####
#.##
####

####
####
##.#
####
"""