x1, y1, x2, y2, x3, y3 = map(int, input().split())
SIZE = max(x1, y1, x2, y2, x3, y3)


def place(grid: list, ad_x: int, ad_y: int, ad_char: str, mode: int) -> tuple:
    """
    mode = 1: sets in the original orientation
    mode = 2: sets in the rotated orientation

    returns the top left coord and bottom right coord and modifies grid if the operation was succesful,
    otherwise returns -666, -666, -666, -666 and clears the attempt from grid.
    """
    free_x = -666
    free_y = -666
    found_free = False
    for y in range(len(grid)):
        if found_free:
            break
        for x in range(len(grid)):
            if found_free:
                break

            if grid[y][x] == "_":
                free_y = y
                free_x = x
                found_free = True

    if not found_free:
        return -666, -666, -666, -666

    needs_reseting = False

    if mode == 1:
        pass
    elif mode == 2:
        ad_x, ad_y = ad_y, ad_x

    if free_x + ad_x > len(grid[0]):
        return -666, -666, -666, -666
    if free_y + ad_y > len(grid[0]):
        return -666, -666, -666, -666

    for y_fill in range(free_y, free_y + ad_y):
        if needs_reseting:
            break
        for x_fill in range(free_x, free_x + ad_x):
            if grid[y_fill][x_fill] != "_":
                needs_reseting = True
                break
            else:
                grid[y_fill][x_fill] = ad_char

    if needs_reseting:
        for y in range(free_y, y_fill):  # type: ignore
            for x in range(free_x, x_fill):  # type: ignore
                grid[y][x] = "_"
        return -666, -666, -666, -666
    else:
        return free_x, free_x + ad_x, free_y, free_y + ad_y


def clear(grid, start_x, end_x, start_y, end_y):
    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            grid[y][x] = "_"


print("")
grid = [["_" for _ in range(SIZE)] for _ in range(SIZE)]
for row in grid:
    print(row)

print("")
print(place(grid, x1, y1, "A", 1))
for row in grid:
    print(row)

print("")
print(place(grid, x2, y2, "B", 1))
for row in grid:
    print(row)

print("")
vals = place(grid, x3, y3, "C", 1)
print(vals)
for row in grid:
    print(row)

print("")
clear(grid, *vals)
for row in grid:
    print(row)

"""
AAAACC
AAAACC
AAAACC
AAAACC

"""
