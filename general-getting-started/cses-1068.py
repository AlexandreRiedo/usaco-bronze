n = int(input())
res: list[str] = [str(n)]

while n != 1:
    if n % 2 == 0:
        n /= 2
    else:
        n = 3 * n + 1
    res.append(f"{n:.0f}")

print(" ".join(res))
