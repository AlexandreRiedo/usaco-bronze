import itertools

GRID_SIZE = 8

grid = [list(input()) for _ in range(GRID_SIZE)]

num_ways = 0

for x_positions in itertools.permutations(range(GRID_SIZE), 8):
    pos_diagonals = set()
    neg_diagonals = set()
    is_valid = True
    for y, x in enumerate(x_positions):
        if grid[y][x] == "*":
            is_valid = False
            break

        pos_diagonal = y + x
        neg_diagonal = y - x

        if pos_diagonal in pos_diagonals:
            is_valid = False
            break
        if neg_diagonal in neg_diagonals:
            is_valid = False
            break

        pos_diagonals.add(pos_diagonal)
        neg_diagonals.add(neg_diagonal)

    if is_valid:
        num_ways += 1

print(num_ways)
