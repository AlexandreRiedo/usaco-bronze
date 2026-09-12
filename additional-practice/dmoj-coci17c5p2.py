from itertools import accumulate
from math import inf

num_rows, num_cols, num_spirals = map(int, input().split())
spirals = []
for _ in range(num_spirals):
    x, y, t = map(int, input().split())
    x -= 1
    y -= 1
    spirals.append((x, y, t))

cells_upto = list(accumulate([1] + [4 * x - 4 for x in range(1, 100, 2)][1:]))
table = [[inf for _ in range(num_cols)] for _ in range(num_rows)]


def assign_spiral(x: int, y: int, direction: int, table: list[list[int]]):
    seen_tl, seen_br = False, False

    val = 1
    table[y][x] = min(val, table[y][x])

    offset = 1
    y -= 1

    while not seen_tl or not seen_br:
        if direction == 0:
            pass
        elif direction == 1:
            print()

        if y == 0 and x == 0:
            seen_tl = True
        if y == len(table) - 1 and x == len(table[0]) - 1:
            seen_br = True


"""
sizes = [4*x - 4 for x in range(1,50,2)]
t = list(accumulate([1]+sizes[1:]))
print(t)
"""
