from collections import deque

from rich import print as rprint

with open("reduce.in") as fin:
    N = int(fin.readline())
    locations = {tuple(map(int, fin.readline().split())) for _ in range(N)}

locations_x = deque(sorted(locations, key=lambda x: x[0]))
locations_y = deque(sorted(locations, key=lambda x: x[1]))

a, b, c, d = locations_x[0], locations_x[-1], locations_y[0], locations_y[-1]
rprint(f"area={(b[0] - a[0]) * (d[1] - c[1])}")
rprint(f"{locations_x=}")
rprint(f"{locations_y=}")

new_a = locations_x[1]
new_b = b if b != a else locations_x[-2]
new_c = c if c != a else locations_y[1]
new_d = d if d != a else locations_y[-2]
rprint(f"{new_a=} {new_b=} {new_c=} {new_d=}")
rprint(f"area sans a={(new_b[0] - new_a[0]) * (new_d[1] - new_c[1])}")

new_b = locations_x[-2]
new_a = a if a != b else locations_x[1]
new_c = c if c != b else locations_y[1]
new_d = d if d != b else locations_y[-2]
rprint(f"{new_a=} {new_b=} {new_c=} {new_d=}")
rprint(f"area sans b={(new_b[0] - new_a[0]) * (new_d[1] - new_c[1])}")

new_c = locations_y[1]
new_a = a if a != c else locations_x[1]
new_b = b if b != c else locations_x[-2]
new_d = d if d != c else locations_y[-2]
rprint(f"{new_a=} {new_b=} {new_c=} {new_d=}")
rprint(f"area sans c={(new_b[0] - new_a[0]) * (new_d[1] - new_c[1])}")

new_d = locations_y[-2]
new_a = a if a != d else locations_x[1]
new_b = b if b != d else locations_x[-2]
new_c = c if c != d else locations_y[1]
rprint(f"{new_a=} {new_b=} {new_c=} {new_d=}")
rprint(f"area sans b={(new_b[0] - new_a[0]) * (new_d[1] - new_c[1])}")

"""
7
-5 25
-3 9
-1 1
0 0
2 4
4 16
6 36
"""

"""
6
1 1
7 8
10 9
8 12
4 100
50 7
"""
