import math

MAX_QUERY = 10**9
NUM_DEALS = math.ceil(math.log2(MAX_QUERY))

n, q = map(int, input().split())

deals = [math.inf] * (NUM_DEALS)
for idx, deal in enumerate(map(int, input().split()[:NUM_DEALS])):
    deals[idx] = deal
for i in range(1, len(deals)):
    deals[i] = min(deals[i], deals[i - 1] * 2)

for _ in range(q):
    x = int(input())
    curr_cost = 0
    ans = math.inf

    while x > 0:
        under = math.floor(math.log2(x))
        over = math.ceil(math.log2(x))

        ans = min(ans, curr_cost + deals[over])
        curr_cost += deals[under]
        x -= 2**under
    ans = min(ans, curr_cost)
    print(ans)
