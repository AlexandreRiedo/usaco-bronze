with open("billboard.in") as f:
    lx1, ly1, lx2, ly2 = map(int, f.readline().split())
    fx1, fy1, fx2, fy2 = map(int, f.readline().split())

area = (lx2 - lx1) * (ly2 - ly1)
if fx1 <= lx1 and fx2 >= lx2 and fy1 <= ly1 and fy2 >= ly2:
    area -= area  # covers everything
elif fx1 <= lx1 and fx2 >= lx2:
    if fy1 <= ly1 and ly1 <= fy2 <= ly2:  # covers the lower
        area -= (lx2 - lx1) * (fy2 - ly1)
    elif ly1 < fy1 < ly2 <= fy2:  # covers the upper
        area -= (lx2 - lx1) * (ly2 - fy1)
elif fy1 <= ly1 and fy2 >= ly2:
    if fx1 <= lx1 and lx1 < fx2 < lx2:  # covers the left
        area -= (fx2 - lx1) * (ly2 - ly1)
    elif fx1 < lx2 and fx2 > lx2:
        area -= (lx2 - fx1) * (ly2 - ly1)  # covers the right

with open("billboard.out", "w") as f:
    f.write(f"{area}\n")