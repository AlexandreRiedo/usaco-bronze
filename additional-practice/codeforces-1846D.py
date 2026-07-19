from math import atan, tan

t = int(input())

for _ in range(t):
    n, d, h = map(int, input().split())
    base_y = list(map(int, input().split()))
    area = 0

    for y, y_next in zip(base_y, base_y[1:]):
        if y + h <= y_next:
            area += (d * h) / 2
        else:
            angle = atan(h / (d / 2))
            to_remove = (y_next - y) / tan(angle)
            top_d = d - (to_remove * 2)
            area += 0.5 * (top_d + d) * (y_next - y)
    area += (d * h) / 2

    print(area)
