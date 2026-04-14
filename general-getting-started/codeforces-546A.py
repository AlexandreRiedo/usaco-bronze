k, n, w = map(int, input().split())

cost = sum([k * i for i in range(1, w + 1)])
print(0 if cost <= n else (cost - n))
