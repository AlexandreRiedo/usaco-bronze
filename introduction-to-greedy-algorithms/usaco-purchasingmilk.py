import math
from collections import defaultdict

from rich import print as rprint

MAX_QUERY = 10**9
NUM_DEALS = math.ceil(math.log2(MAX_QUERY) + 1)

n, q = map(int, input().split())

deals = [math.inf] * (NUM_DEALS)
per_bucket_deals = defaultdict(float)
for idx, deal in enumerate(map(int, input()[:NUM_DEALS].split())):
    deals[idx] = deal

per_bucket_deals[0] = deals[0]
for i in range(1, len(deals)):
    deals[i] = min(deals[i], deals[i - 1] * 2)
    per_bucket_deals[i] = deals[i] / (2**i)

# rprint(f"{deals=}")
# rprint(f"{per_bucket_deals=}")
# rprint(f"{list(per_bucket_deals.items())[:5]=}")
# rprint(f"{min(list(per_bucket_deals.items())[:5], key=lambda x: (x[1], -x[0]))}")

for _ in range(q):
    x = int(input())

    ans = 0
    while x > 0:
        exponent = math.floor(math.log2(x))

    rprint(ans)


"""
CLAUDE hint:
5 1
5 6 7 8 100
1 2 4 8 16
11
-> 15 (4+8=12, => 15), not 16 (1+2+8=11, -> 5+6+8=19)
"""
