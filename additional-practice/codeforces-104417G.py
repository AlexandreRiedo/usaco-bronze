from collections import defaultdict
from operator import itemgetter

for _ in range(int(input())):
    n = int(input())
    seq = list(map(int, input().split()))
    ans = 0
    edges = defaultdict(int)

    for i in range(n):
        score = 0
        for j in range(i + 1, n):
            if (i + 1) - (j + 1) == seq[i] - seq[j]:
                score = max(score, seq[i] + seq[j])
                edges[(i+1,j+1)] = seq[i] + seq[j]
        ans += score

    from rich import print as rprint

    sort_edges = []
    for k, v in edges.items():
        sort_edges.append((*k, v))
    sort_edges.sort(key=itemgetter(2), reverse=True)
    sort_edges = [x for x in sort_edges if x[2] > 0]
    rprint(f"{ans=}")
    rprint(f"{edges=}")
    rprint(f"{sort_edges=}\n")

"""
O(n*log(n)) is the max
"""

"""
import random; SIZE = 10**4; print(1); print(SIZE); print(*[random.randint(-10**9, 10**9) for _ in range(SIZE)], sep=" ")
py -c 'import random; SIZE = 10**2; print(1); print(SIZE); print(*[random.randint(-10**2, 10**2) for _ in range(SIZE)], sep=" ")' | py ./codeforces-104417G.py
"""