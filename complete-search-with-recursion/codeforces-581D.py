x1, y1, x2, y2, x3, y3 = map(int, input().split())
SIZE = max(x1, y1, x2, y2, x3, y3)
LOGO_CHAR = {0: "A", 1: "B", 2: "C"}
logos = [(x1, y1), (x2, y2), (x3, y3)]


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


def clear(grid: list, start_x: int, end_x: int, start_y: int, end_y: int):
    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            grid[y][x] = "_"


grid = [["_" for _ in range(SIZE)] for _ in range(SIZE)]
is_solved = False


def solve(grid: list, used_logos=set()):
    global is_solved

    if len(used_logos) == 3:
        for y in range(SIZE):
            for x in range(SIZE):
                if grid[y][x] == "_":
                    return
        print(SIZE)
        for row in grid:
            print("".join(row))
        is_solved = True
        exit()

    for logo_idx, logo in enumerate(logos):
        if logo_idx in used_logos:
            continue

        ad_x, ad_y = logo
        if (coords := place(grid, ad_x, ad_y, LOGO_CHAR[logo_idx], 1)) != (
            -666,
            -666,
            -666,
            -666,
        ):
            used_logos.add(logo_idx)
            solve(grid, used_logos)
            clear(grid, *coords)
            used_logos.remove(logo_idx)
        if (coords := place(grid, ad_x, ad_y, LOGO_CHAR[logo_idx], 2)) != (
            -666,
            -666,
            -666,
            -666,
        ):
            used_logos.add(logo_idx)
            solve(grid, used_logos)
            clear(
                grid,
                *coords,
            )
            used_logos.remove(logo_idx)


solve(grid)
if not is_solved:
    print("-1")
