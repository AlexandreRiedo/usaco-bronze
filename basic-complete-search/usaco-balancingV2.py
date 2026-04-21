import itertools
import sys
from math import inf
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


def get_max_m(vertical, horizontal, cows):
    bottom_left, top_left, bottom_right, top_right = 0, 0, 0, 0
    for cow in cows:
        if cow.x < vertical and cow.y < horizontal:
            bottom_left += 1
        elif cow.x < vertical and cow.y > horizontal:
            top_left += 1
        elif cow.x > vertical and cow.y < horizontal:
            bottom_right += 1
        elif cow.x > vertical and cow.y > horizontal:
            top_right += 1

    return max(bottom_left, top_left, bottom_right, top_right)


sys.stdin = open("balancing.in", "r")
sys.stdout = open("balancing.out", "w")

num_cows, max_distance = map(int, input().split())
cows = [Point(*map(int, input().split())) for _ in range(num_cows)]

vertical_candidates = set(cow.x + 1 for cow in cows)
vertical_candidates.add(0)

horizontal_candidates = set(cow.y + 1 for cow in cows)
horizontal_candidates.add(0)


best = inf
for vertical, horizontal in itertools.product(
    vertical_candidates, horizontal_candidates
):
    best = min(best, get_max_m(vertical, horizontal, cows))

print(best)
