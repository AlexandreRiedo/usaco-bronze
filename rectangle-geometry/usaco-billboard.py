def is_overlapping(x1, y1, x2, y2, ix1, iy1, ix2, iy2):
    if ix2 <= x1 or iy2 <= y1:  # left, bottom
        return False
    elif ix1 >= x2 or iy1 >= y2:  # right, top
        return False
    else:
        return True


def clamp(x1, y1, x2, y2, cx1, cy1, cx2, cy2):
    return max(x1, cx1), max(y1, cy1), min(x2, cx2), min(y2, cy2)


def area(x1, y1, x2, y2):
    return abs(x2 - x1) * abs(y2 - y1)


with open("billboard.in") as f:
    ax1, ay1, ax2, ay2 = map(int, f.readline().split())
    bx1, by1, bx2, by2 = map(int, f.readline().split())
    tx1, ty1, tx2, ty2 = map(int, f.readline().split())

area_a = area(ax1, ay1, ax2, ay2)
if is_overlapping(ax1, ay1, ax2, ay2, tx1, ty1, tx2, ty2):
    area_a -= area(*clamp(ax1, ay1, ax2, ay2, tx1, ty1, tx2, ty2))

area_b = area(bx1, by1, bx2, by2)
if is_overlapping(bx1, by1, bx2, by2, tx1, ty1, tx2, ty2):
    area_b -= area(*clamp(bx1, by1, bx2, by2, tx1, ty1, tx2, ty2))

answer = area_a + area_b

with open("billboard.out", "w") as f:
    f.write(f"{answer}\n")
