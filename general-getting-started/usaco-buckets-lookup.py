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

cows = abs(barn.x - lake.x) + abs(barn.y - lake.y) - 1

if barn.y == lake.y == rock.y and (
    barn.x < rock.x < lake.x or barn.x > rock.x > lake.x
):
    cows += 2

if barn.x == lake.x == rock.x and (
    barn.y < rock.y < lake.y or barn.y > rock.y > lake.y
):
    cows += 2

print(cows)
