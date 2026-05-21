import sys
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


def valid_back_shift(point, right, down):
    return (point.x - right) >= 0 and (point.y - down) >= 0


num_tests = int(sys.stdin.readline().strip())

for _ in range(num_tests):
    # 0. Setup
    photo_size, shift_right, shift_down = map(int, sys.stdin.readline().strip().split())
    count = 0

    photo = [list(sys.stdin.readline().strip()) for _ in range(photo_size)]

    # 1. Algorithm
    for y in range(photo_size - 1, -1, -1):
        for x in range(photo_size - 1, -1, -1):
            char = photo[y][x]
            if char == "W":
                continue
            if char == "G":
                if x >= shift_right and y >= shift_down:
                    if photo[y - shift_down][x - shift_right] == "W":
                        count += 1
                else:
                    count += 1
            if char == "B":
                if x >= shift_right and y >= shift_down:
                    if photo[y - shift_down][x - shift_right] == "W":
                        count = -1
                        break
                    else:
                        count += 1
                count += 1

    # x. Output!
    sys.stdout.write(f"{count}\n")

    # Testing
    from rich import print as rprint

    rprint(photo)

"""
CASE 1
1
5 1 2
GWGWW
WGWWW
WBWGW
WWWWW
WWGWW
-> 4

*.*..
.*...
.*...
.....
.....

.....
.....
.*.*.
..#..
..*..
"""

"""
CASE 2
1
3 1 1
WWW
WBW
WWW
-> -1

*..
.*.
...
can't work !

WWWWBWWWW
"""


"""
CASE 3
3 1 0
GGB
GGW
WWW
-> 4

***
*..
...

..*
.*.
...
"""
