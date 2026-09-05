import math

MAX_QUERY = 10**9
NUM_DEALS = math.ceil(math.log2(MAX_QUERY))

n, q = map(int, input().split())

deals = [math.inf] * (NUM_DEALS)
for idx, deal in enumerate(map(int, input().split())):
    deals[idx] = deal
for i in range(1, len(deals)):
    deals[i] = min(deals[i], deals[i - 1] * 2)

for _ in range(q):
    x = list(map(int, bin(int(input()))[:1:-1]))

    ans, exponent = 0, 0
    for exponent, code in enumerate(x):
        ans += deals[exponent] * code

    ans = min(ans, deals[exponent + 1])

    print(ans)

"""
CLAUDE Hint:
5 1
5 6 7 8 100
11
"""
