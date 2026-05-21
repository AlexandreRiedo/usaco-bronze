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

    points_black = []
    points_grey = []
    points_white = []

    photo_result = []
    photo_init = [["." for _ in range(photo_size)] for _ in range(photo_size)]
    photo_shifted = [["." for _ in range(photo_size)] for _ in range(photo_size)]

    for y in range(photo_size):
        row = []
        for x, char in enumerate(sys.stdin.readline().strip()):
            row.append(char)
            if char == "W":
                points_white.append(Point(x, y))
            elif char == "G":
                points_grey.append(Point(x, y))
            elif char == "B":
                points_black.append(Point(x, y))
        photo_result.append(row)

    points_grey_set = set(points_grey)
    points_black_set = set(points_black)

    # 1. Solve for black
    for point in points_black:
        back_shifted = Point(point.x - shift_right, point.y - shift_down)
        shifted = Point(point.x + shift_right, point.y + shift_down)

        if (
            not valid_back_shift(point, shift_right, shift_down)
            or photo_result[back_shifted.y][back_shifted.x] == "W"
        ):
            count = -1
            break
        else:
            # Mark the points necessary for a black result
            if photo_init[point.y][point.x] == ".":
                count += 1
                photo_init[point.y][point.x] = "*"
            if photo_init[back_shifted.y][back_shifted.x] == ".":
                count += 1
                photo_init[back_shifted.y][back_shifted.x] = "*"
            photo_shifted[point.y][point.x] = "*"

            # Greedy : re-use the point as a shifted point if needed
            if shifted in points_grey_set or shifted in points_black_set:
                photo_shifted[shifted.y][shifted.x] = "*"
    # 2. Solve for grey
    else:
        for point in points_grey:
            shifted = Point(point.x + shift_right, point.y + shift_down)

            # Skip if there's already a point on the initial or the shifted photo
            if (
                photo_init[point.y][point.x] == "*"
                or photo_shifted[point.y][point.x] == "*"
            ):
                continue
            # Add the point otherwise to the initial photo
            else:
                photo_init[point.y][point.x] = "*"
                count += 1

                # Greedy : Use the shifted point if it can satisfy a grey point further down
                if shifted in points_grey_set:
                    if point != shifted:
                        photo_shifted[shifted.y][shifted.x] = "*"

    # 3. Output!
    sys.stdout.write(f"{count}\n")

    # from rich import print as rprint

    # rprint(f"{points_black=}\n{points_grey=}\n{points_white=}")
    # rprint(f"{count=}")
    # for row in photo_init:
    #     rprint(row)
    # rprint("")
    # for row in photo_shifted:
    #     rprint(row)
    # rprint("---------")


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
