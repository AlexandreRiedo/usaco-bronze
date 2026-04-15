import sys
from collections import defaultdict
from math import inf

sys.stdin = open("mowing.in", "r")
sys.stdout = open("mowing.out", "w")


class Point:
    def __init__(self, x, y) -> None:
        self.x: int = x
        self.y: int = y

    def __repr__(self):
        return f"Point(x={self.x} y={self.y})"

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y


num_moves = int(input())
moves = []
for _ in range(num_moves):
    direction, num_steps = input().split()
    moves.append((direction, int(num_steps)))

x = inf
position_to_timeline = defaultdict(list)
time = 0
prev_location = Point(0, 0)
position_to_timeline[prev_location].append(time)

for direction, steps in moves:
    for step in range(steps):
        time += 1
        direction_map = {"N": (0, 1), "E": (1, 0), "W": (-1, 0), "S": (0, -1)}
        dx, dy = direction_map[direction]
        curr_location = Point(prev_location.x + dx, prev_location.y + dy)

        if curr_location in position_to_timeline:
            x = min(x, time - position_to_timeline[curr_location][-1])
        position_to_timeline[curr_location].append(time)

        prev_location = curr_location

print(x if x != inf else "-1")
