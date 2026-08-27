for _ in range(int(input())):
    a, b, c = map(int, input().split())
    lead = max(a, b, c)

    if sum([a == lead, b == lead, c == lead]) == 1:
        default = 0
    else:
        default = 1

    print(
        lead - a + 1 if a != lead else default,
        lead - b + 1 if b != lead else default,
        lead - c + 1 if c != lead else default,
    )
