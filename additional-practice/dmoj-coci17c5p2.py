from math import inf


def add(x, y, val, table, x_len, y_len):
    if 0 <= x < x_len and 0 <= y < y_len:
        table[y][x] = min(val, table[y][x])


def assign_spiral(x: int, y: int, direction: int, table: list[list]):
    val = 1
    zone = 2
    x_len, y_len = len(table[0]), len(table)
    init_x, init_y = x, y
    cap = max(max(init_x, x_len - init_x), max(init_y, y_len - init_y))

    add(x, y, val, table, x_len, y_len)
    y -= 1

    while (zone / 2) < cap:
        if direction == 0:
            for x in range(x, x + zone):
                val += 1
                add(x, y, val, table, x_len, y_len)
            for y in range(y + 1, y + 1 + zone):
                val += 1
                add(x, y, val, table, x_len, y_len)
            for x in range(x - 1, x - 1 - zone, -1):
                val += 1
                add(x, y, val, table, x_len, y_len)
            for y in range(y - 1, y - 1 - zone, -1):
                val += 1
                add(x, y, val, table, x_len, y_len)
        else:
            for x in range(x, x - zone, -1):
                val += 1
                add(x, y, val, table, x_len, y_len)
            for y in range(y + 1, y + 1 + zone):
                val += 1
                add(x, y, val, table, x_len, y_len)
            for x in range(x + 1, x + 1 + zone):
                val += 1
                add(x, y, val, table, x_len, y_len)
            for y in range(y - 1, y - 1 - zone, -1):
                val += 1
                add(x, y, val, table, x_len, y_len)

        y -= 1
        zone += 2


num_rows, num_cols, num_spirals = map(int, input().split())
table = [[inf for _ in range(num_cols)] for _ in range(num_rows)]
for _ in range(num_spirals):
    y, x, t = map(int, input().split())
    x -= 1
    y -= 1
    assign_spiral(x, y, t, table)

for row in table:
    print(*row)
