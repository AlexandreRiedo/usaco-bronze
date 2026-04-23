import itertools
from math import inf


def calculate_shifting_ranges(grid, size):
    """
    1st value: the amount you can shift to the left
    2nd value: the amount you can shift to the right
    3rd value: the amount you can shift to the top
    4th value: the amount you can shift to the bottom
    """
    left_most = inf
    right_most = -inf
    top_most = inf
    bottom_most = -inf

    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == "#":
                left_most = min(left_most, x)
                right_most = max(right_most, x)
                top_most = min(top_most, y)
                bottom_most = max(bottom_most, y)

    return left_most, size - (right_most + 1), top_most, size - (bottom_most + 1)


def shift_piece(grid, size, x_shift, y_shift):
    new_grid = [["." for _ in range(size)] for _ in range(size)]

    for y in range(size):
        for x in range(size):
            char = grid[y][x]
            if char == "#":
                new_grid[y + y_shift][x + x_shift] = "#"

    return new_grid


def combine_pieces(grid_a, grid_b, size):
    new_grid = []

    for y in range(size):
        row = []
        for x in range(size):
            if grid_a[y][x] == grid_b[y][x] == "#":
                return False
            elif grid_a[y][x] == "#":
                row.append("#")
            elif grid_b[y][x] == "#":
                row.append("#")
            else:
                row.append(".")

        new_grid.append(row)

    return new_grid


def verify(original, testing, size):
    for y in range(size):
        for x in range(size):
            if original[y][x] != testing[y][x]:
                return False
    return True


with open("bcs.in") as f:
    size, num_pieces = map(int, f.readline().split())

    original = [[item for item in f.readline().strip()] for _ in range(size)]
    pieces = [
        [[item for item in f.readline().strip()] for _ in range(size)]
        for _ in range(num_pieces)
    ]

shifting_ranges = {id: (0, 0, 0, 0) for id in range(num_pieces)}
for idx, piece in enumerate(pieces):
    shifting_ranges[idx] = calculate_shifting_ranges(piece, size)  # type: ignore

for piece_a_idx in range(num_pieces):
    for piece_b_idx in range(piece_a_idx, num_pieces):
        a_shift_x_range = range(
            -shifting_ranges[piece_a_idx][0], shifting_ranges[piece_a_idx][1] + 1
        )
        a_shift_y_range = range(
            -shifting_ranges[piece_a_idx][2], shifting_ranges[piece_a_idx][3] + 1
        )
        b_shift_x_range = range(
            -shifting_ranges[piece_b_idx][0], shifting_ranges[piece_b_idx][1] + 1
        )
        b_shift_y_range = range(
            -shifting_ranges[piece_b_idx][2], shifting_ranges[piece_b_idx][3] + 1
        )

        for a_shift_x, a_shift_y, b_shift_x, b_shift_y in itertools.product(
            a_shift_x_range, a_shift_y_range, b_shift_x_range, b_shift_y_range
        ):
            new_a = shift_piece(pieces[piece_a_idx], size, a_shift_x, a_shift_y)
            new_b = shift_piece(pieces[piece_b_idx], size, b_shift_x, b_shift_y)

            combined = combine_pieces(new_a, new_b, size)

            if combined:
                if verify(original, combined, size):
                    correct_a = piece_a_idx + 1
                    correct_b = piece_b_idx + 1

                    correct_a, correct_b = (
                        min(correct_a, correct_b),
                        max(correct_a, correct_b),
                    )
                    break

with open("bcs.out", "w") as f:
    f.write(f"{correct_a} {correct_b}")  # type: ignore
