with open("cowtip.in") as file:
    grid_size = int(file.readline().strip())
    grid = [
        list(map(lambda x: bool(int(x)), file.readline().strip()))
        for _ in range(grid_size)
    ]


def find_greedy_coords(grid: list) -> tuple:
    """
    returns -1, -1 if there is no 'True' in the grid
    """
    greedy_x = -1
    greedy_y = -1
    for y in range(len(grid)):
        for x in range(len(grid)):
            if grid[y][x]:
                if y + x > greedy_y + greedy_x:
                    greedy_y = y
                    greedy_x = x

    return greedy_x, greedy_y


def flip_cows(grid: list, flip_x: int, flip_y: int):
    """
    flips the cows of the grid in place
    """
    for y in range(flip_y + 1):
        for x in range(flip_x + 1):
            grid[y][x] = not grid[y][x]


count = 0
greedy_coords = find_greedy_coords(grid)
while greedy_coords != (-1, -1):
    greedy_x, greedy_y = greedy_coords
    flip_cows(grid, greedy_x, greedy_y)
    count += 1
    greedy_coords = find_greedy_coords(grid)

with open("cowtip.out", "w") as file:
    file.write(f"{count}\n")
