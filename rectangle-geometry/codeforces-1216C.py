x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())


# USACO guide's intersection area
def inter_area(s1, s2) -> int:
    bl_a_x, bl_a_y, tr_a_x, tr_a_y = s1[0], s1[1], s1[2], s1[3]
    bl_b_x, bl_b_y, tr_b_x, tr_b_y = s2[0], s2[1], s2[2], s2[3]

    calc = (min(tr_a_x, tr_b_x) - max(bl_a_x, bl_b_x)) * (
        min(tr_a_y, tr_b_y) - max(bl_a_y, bl_b_y)
    )

    if calc < 0:
        return 0
    else:
        return calc


def solve(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    # clamp
    x3, y3 = min(max(x3, x1), x2), min(max(y3, y1), y2)
    x4, y4 = max(min(x4, x2), x1), max(min(y4, y2), y1)
    x5, y5 = min(max(x5, x1), x2), min(max(y5, y1), y2)
    x6, y6 = max(min(x6, x2), x1), max(min(y6, y2), y1)

    # area math
    area_b1 = (x4 - x3) * (y4 - y3)
    area_b2 = (x6 - x5) * (y6 - y5)
    area_intersection = inter_area([x3, y3, x4, y4], [x5, y5, x6, y6])
    area_white = (x2 - x1) * (y2 - y1)

    # solve
    if area_b1 + area_b2 - area_intersection == area_white:
        return "NO"
    else:
        return "YES"


print(solve(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6))
