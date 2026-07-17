def find_bbox(color, canvas):
    top = right = bottom = left = -1
    for y, row in enumerate(canvas):
        for x, cell in enumerate(row):
            if cell != color:
                continue

            if top == -1:
                top = y
            if right == -1:
                right = x
            if bottom == -1:
                bottom = y
            if left == -1:
                left = x

            top = min(top, y)
            right = max(right, x)
            bottom = max(bottom, y)
            left = min(left, x)

    return [left, top, right, bottom]


with open("art.in") as f:
    N = int(f.readline())
    canvas = [[int(num) for num in f.readline().strip()] for _ in range(N)]

colors = {color for row in canvas for color in row} - {0}
deps = {color: set() for color in colors}  # If a color has deps, it can't be first

for color in colors:
    left, top, right, bottom = find_bbox(color, canvas)
    for y in range(top, bottom + 1):
        for x in range(left, right + 1):
            if canvas[y][x] != color:
                deps[canvas[y][x]].add(color)

with open("art.out", "w") as f:
    ans = sum(1 for dep in deps.values() if len(dep) == 0)
    f.write(f"{ans}\n")
