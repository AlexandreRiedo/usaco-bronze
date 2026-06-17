with open("square.in") as f:
    ax1, ay1, ax2, ay2 = map(int, f.readline().split())
    bx1, by1, bx2, by2 = map(int, f.readline().split())

with open("square.out", "w") as f:
    x_size = max(ax1, ax2, bx1, bx2) - min(ax1, ax2, bx1, bx2)
    y_size = max(ay1, ay2, by1, by2) - min(ay1, ay2, by1, by2)
    answer = max(x_size, y_size) ** 2
    f.write(f"{answer}\n")
