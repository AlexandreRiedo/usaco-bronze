import math


def is_fittable(W, H, x1, y1, x2, y2, w, h):
    # Top
    if (H - y2) >= h and (W - 0) >= w:
        return True
    # Right
    elif (H - 0) >= h and (W - x2) >= w:
        return True
    # Bottom
    elif (y1 - 0) >= h and (W - 0) >= w:
        return True
    # Left
    elif (H - 0) >= h and (x1 - 0) >= w:
        return True
    # Can't fit otherwise
    else:
        return False


def diag(x, y):
    return math.sqrt(x**2 + y**2)


tests = int(input())
for _ in range(tests):
    W, H = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    w, h = map(int, input().split())

    distances = []
    dist_top = h - min((H - y2), h) if y1 - 0 >= h - (H - y2) else None
    dist_right = w - min((W - x2), w) if x1 - 0 >= w - (W - x2) else None
    dist_bottom = h - min((y1 - 0), h) if H - y2 >= h - (y1 - 0) else None
    dist_left = w - min((x1 - 0), w) if W - x2 >= w - (x1 - 0) else None

    # Top
    if (dist_top is not None) and is_fittable(
        W, H, x1, y1 - dist_top, x2, y2 - dist_top, w, h
    ):
        distances.append(dist_top)
    # Right
    if (dist_right is not None) and is_fittable(
        W, H, x1 - dist_right, y1, x2 - dist_right, y2, w, h
    ):
        distances.append(dist_right)
    # Bottom
    if (dist_bottom is not None) and is_fittable(
        W, H, x1, y1 + dist_bottom, x2, y2 + dist_bottom, w, h
    ):
        distances.append(dist_bottom)
    # Left
    if (dist_left is not None) and is_fittable(
        W, H, x1 + dist_left, y1, x2 + dist_left, y2, w, h
    ):
        distances.append(dist_left)

    # Right-Top
    if (
        (dist_top is not None)
        and (dist_right is not None)
        and is_fittable(
            W, H, x1 - dist_right, y1 - dist_top, x2 - dist_right, y2 - dist_top, w, h
        )
    ):
        distances.append(diag(dist_right, dist_top))
    # Right-Bottom
    if (
        (dist_bottom is not None)
        and (dist_right is not None)
        and is_fittable(
            W,
            H,
            x1 - dist_right,
            y1 + dist_bottom,
            x2 - dist_right,
            y2 + dist_bottom,
            w,
            h,
        )
    ):
        distances.append(diag(dist_right, dist_bottom))
    # Left-Bottom
    if (
        (dist_bottom is not None)
        and (dist_left is not None)
        and is_fittable(
            W,
            H,
            x1 + dist_left,
            y1 + dist_bottom,
            x2 + dist_left,
            y2 + dist_bottom,
            w,
            h,
        )
    ):
        distances.append(diag(dist_left, dist_bottom))
    # Left-Top
    if (
        (dist_top is not None)
        and (dist_left is not None)
        and is_fittable(
            W, H, x1 + dist_left, y1 - dist_top, x2 + dist_left, y2 - dist_top, w, h
        )
    ):
        distances.append(diag(dist_left, dist_top))

    print(min(distances, default=-1))
