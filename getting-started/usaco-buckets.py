import math
import sys

SIZE = 10


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


sys.stdin = open("buckets.in", "r")
data = [item.strip() for item in sys.stdin.readlines()]
sys.stdout = open("buckets.out", "w")

grid = []
barn = Point(0, 0)
lake = Point(0, 0)
rock = Point(0, 0)

for y in range(SIZE):
    row = []
    for x in range(SIZE):
        char = data[y][x]
        row.append(char)

        if char == "B":
            barn = Point(x, y)
        elif char == "R":
            rock = Point(x, y)
        elif char == "L":
            lake = Point(x, y)
    grid.append(row)

cursor = barn
cows = 0
while not (
    (cursor.x == lake.x - 1 and cursor.y == lake.y)
    or (cursor.x == lake.x + 1 and cursor.y == lake.y)
    or (cursor.x == lake.x and cursor.y == lake.y + 1)
    or (cursor.x == lake.x and cursor.y == lake.y - 1)
):
    possibilities = []

    if Point(cursor.x + 1, cursor.y) != rock and cursor.x != SIZE - 1:
        possibilities.append(Point(cursor.x + 1, cursor.y))
    if Point(cursor.x - 1, cursor.y) != rock and cursor.x != 0:
        possibilities.append(Point(cursor.x - 1, cursor.y))
    if Point(cursor.x, cursor.y + 1) != rock and cursor.y != SIZE - 1:
        possibilities.append(Point(cursor.x, cursor.y + 1))
    if Point(cursor.x, cursor.y - 1) != rock and cursor.y != 0:
        possibilities.append(Point(cursor.x, cursor.y - 1))

    possibilities.sort(
        key=lambda point: math.sqrt(
            abs(lake.x - point.x) ** 2 + abs(lake.y - point.y) ** 2
        )
    )

    cursor = possibilities[0]
    cows += 1

print(cows)
