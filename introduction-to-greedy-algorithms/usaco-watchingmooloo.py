num_days, cost = map(int, input().split())
days = list(map(int, input().split()))

res = 1 + cost
for a, b in zip(days, days[1:]):
    if b - a > 1 + cost:
        res += 1 + cost
    else:
        res += b - a

print(res)
