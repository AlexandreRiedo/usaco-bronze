import sys
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


sys.stdin = open("triangles.in", "r")
sys.stdout = open("triangles.out", "w")

num_points = int(input())
points = []
for _ in range(num_points):
    x, y = map(int, input().split())
    points.append(Point(x, y))

max_area = 0
for a in points:
    for b in points:
        for c in points:
            if a.x == b.x and b.y == c.y:
                area = abs(a.y - b.y) * abs(b.x - c.x)
                max_area = max(max_area, area)

print(max_area)
