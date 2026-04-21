import itertools
import sys
from collections import defaultdict
from math import inf
from typing import NamedTuple

from rich import print as rprint


class Point(NamedTuple):
    x: int
    y: int


class Record(NamedTuple):
    left: int
    right: int
    m: int
    pos: int


def get_min_m(vertical, horizontal, cows):
    bottom_left, top_left, bottom_right, top_right = 0, 0, 0, 0
    for cow in cows:
        if cow.x < vertical.pos and cow.y < horizontal.pos:
            bottom_left += 1
        elif cow.x < vertical.pos and cow.y > horizontal.pos:
            top_left += 1
        elif cow.x > vertical.pos and cow.y < horizontal.pos:
            bottom_right += 1
        elif cow.x > vertical.pos and cow.y > horizontal.pos:
            top_right += 1

    return max(bottom_left, top_left, bottom_right, top_right)


sys.stdin = open("balancing.in", "r")
# sys.stdout = open("balancing.out", "w")

num_cows, max_distance = map(int, input().split())
cows = [Point(*map(int, input().split())) for _ in range(num_cows)]
cows_x = defaultdict(int)
cows_y = defaultdict(int)

for cow in cows:
    cows_x[cow.x] += 1
    cows_y[cow.y] += 1

# Finding the best vertical divisions
cows_x_split = [Record(0, 0, 0, 0) for _ in range(len(cows_x) + 1)]
cows_x_split[0] = Record(0, num_cows, max(0, num_cows), 0)

for index, (pos, count) in enumerate(sorted(cows_x.items(), key=lambda kv: kv[0])):
    cows_x_split[index + 1] = Record(
        cows_x_split[index].left + count,
        cows_x_split[index].right - count,
        max(cows_x_split[index].left + count, cows_x_split[index].right - count),
        pos + 1,
    )

vertical_candidates = []
cows_x_split.sort(key=lambda x: x.m)
best_x_m = cows_x_split[0].m
for record in cows_x_split:
    if record.m == best_x_m:
        vertical_candidates.append(record)
    else:
        break

# Finding the best horizontal divisions
cows_y_split = [Record(0, 0, 0, 0) for _ in range(len(cows_y) + 1)]
cows_y_split[0] = Record(0, num_cows, max(0, num_cows), 0)

for index, (pos, count) in enumerate(sorted(cows_y.items(), key=lambda kv: kv[0])):
    cows_y_split[index + 1] = Record(
        cows_y_split[index].left + count,
        cows_y_split[index].right - count,
        max(cows_y_split[index].left + count, cows_y_split[index].right - count),
        pos + 1,
    )

horizontal_candidates = []
cows_y_split.sort(key=lambda x: x.m)
best_y_m = cows_y_split[0].m
for record in cows_y_split:
    if record.m == best_y_m:
        horizontal_candidates.append(record)
    else:
        break

# Finding m
best = inf
for horizontal, vertical in itertools.product(
    horizontal_candidates, vertical_candidates
):
    rprint(f"{vertical=} {horizontal=}")
    best = min(best, get_min_m(vertical, horizontal, cows))

rprint("")
rprint(f"{cows_x=}")
rprint(f"{cows_y=}")
rprint(f"{sorted(cows_x_split, key= lambda x: x.pos)=}")
rprint(f"{vertical_candidates=}")
rprint(f"{horizontal_candidates=}")
rprint("")
rprint(f"{best=}")
# print(best)

"""
THIS BREAKS! CF. DESMOS
6 10
7 3
5 5
5 7
3 8
3 7
5 3
"""
