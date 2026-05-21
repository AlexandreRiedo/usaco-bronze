import sys
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


def solve(photo, photo_size, shift_right, shift_down):
    used_pos = set()

    for y in range(photo_size):
        for x in range(photo_size):
            char = photo[y][x]
            pos = (x, y)
            back_pos = (x - shift_right, y - shift_down)
            back_char = (
                photo[y - shift_down][x - shift_right]
                if ((y - shift_down) >= 0 and (x - shift_right) >= 0)
                else None
            )

            if char == "W":
                continue
            elif char == "G":
                if back_pos not in used_pos:
                    used_pos.add(pos)
            elif char == "B":
                if back_char is None or back_char == "W":
                    return -1
                else:
                    if back_pos not in used_pos and back_pos is not None:
                        used_pos.add(pos)
                        used_pos.add(back_pos)
                    else:
                        used_pos.add(pos)

    return len(used_pos)


num_tests = int(sys.stdin.readline().strip())

for _ in range(num_tests):
    # 0. Setup
    photo_size, shift_right, shift_down = map(int, sys.stdin.readline().strip().split())
    photo = [list(sys.stdin.readline().strip()) for _ in range(photo_size)]

    # 1. Algorithm
    answer = solve(photo, photo_size, shift_right, shift_down)

    # 2. Output!
    sys.stdout.write(f"{answer}\n")

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
