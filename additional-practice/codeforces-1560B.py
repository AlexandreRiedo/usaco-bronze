for _ in range(int(input())):
    a, b, c = map(int, input().split())
    a, b = min(a, b), max(a, b)
    x = b - a

    if (b < 2 * a) or c > 2 * (x := (b - a)):
        print(-1)
    else:
        ans = c + x if c <= x else max(c - x, 1)
        print(ans)
