import copy


def find_bbox(color, canvas):
    top = right = bottom = left = None
    for y, row in enumerate(canvas):
        for x, cell in enumerate(row):
            if cell != color:
                continue

            if top is None:
                top = y
            if right is None:
                right = x
            if bottom is None:
                bottom = y
            if left is None:
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
bboxes = {color: [] for color in colors}  # [TLx, TLy, BRx, BRy]
deps = {color: set() for color in colors}  # If a color has deps, it can't be first

for color in colors:
    bboxes[color] = find_bbox(color, canvas)

for color_1st in colors:
    other_colors = [color for color in colors if color != color_1st]
    canvas_edit = copy.deepcopy(canvas)

    # Paint over the color_1st's bbox
    for y, row in enumerate(canvas_edit):
        for x, cell in enumerate(row):
            if (
                bboxes[color_1st][0] <= x <= bboxes[color_1st][2]
                and bboxes[color_1st][1] <= y <= bboxes[color_1st][3]
            ):
                canvas_edit[y][x] = color_1st

    # Check if bbox has been changed -> other_color is dep on color_1st
    for other_color in other_colors:
        if bboxes[other_color] != find_bbox(other_color, canvas_edit):
            deps[other_color].add(color_1st)

from rich import print as rprint

rprint(f"{deps=}")

with open("art.out", "w") as f:
    ans = sum(1 for dep in deps.values() if len(dep) == 0)
    rprint(f"{ans=}")
    f.write(f"{ans}\n")
