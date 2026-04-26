GRID_SIZE = 8

blocked = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
for r in range(GRID_SIZE):
    row = input()
    for c in range(GRID_SIZE):
        blocked[r][c] = row[c] == "*"

rows_taken = [False] * GRID_SIZE
diag1 = [False] * (GRID_SIZE * 2 - 1)
diag2 = [False] * (GRID_SIZE * 2 - 1)

valid_num = 0


def search_queens(c: int = 0):
    global valid_num

    if c == GRID_SIZE:
        valid_num += 1
        return

    for r in range(GRID_SIZE):
        row_open = not rows_taken[r]
        diag_open = not diag1[r + c] and not diag2[r - c + GRID_SIZE - 1]
        if not blocked[r][c] and row_open and diag_open:
            rows_taken[r] = diag1[r + c] = diag2[r - c + GRID_SIZE - 1] = True
            search_queens(c + 1)
            rows_taken[r] = diag1[r + c] = diag2[r - c + GRID_SIZE - 1] = False


search_queens()
print(valid_num)
