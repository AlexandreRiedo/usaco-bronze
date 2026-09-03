import math

n, q = map(int, input().split())

deals = [math.inf] * (10**5 + 100)
for idx, deal in enumerate(map(int, input().split())):
    deals[idx] = deal
for i in range(1, len(deals)):
    deals[i] = min(deals[i], deals[i - 1] * 2)

for _ in range(q):
    x = list(map(int, bin(int(input()))[:1:-1]))

    ans = 0
    exponent = 0
    for exponent, code in enumerate(x):
        ans += deals[exponent] * code

    ans = min(ans, deals[exponent + 1])

    print(ans)
