import sys
from collections import defaultdict
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


sys.stdin = open("balancing.in", "r")

num_cows, max_distance = map(int, input().split())
cows = [Point(*map(int, input().split())) for _ in range(num_cows)]
cows_x = defaultdict(int)
cows_y = defaultdict(int)

for cow in cows:
    cows_x[cow.x] += 1
    cows_y[cow.y] += 1

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
        vertical_candidates.append(record.pos)
    else:
        break

rprint(f"{cows_x=}")
rprint(f"{cows_y=}")
rprint(f"{sorted(cows_x_split, key= lambda x: x.pos)=}")
rprint(f"{vertical_candidates=}")

"""
6 10
7 3
5 5
9 7
3 1
7 7
9 3
"""
