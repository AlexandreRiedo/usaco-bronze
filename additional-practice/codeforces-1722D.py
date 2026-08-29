from itertools import pairwise
from math import ceil

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    x = 0

    for a, b in pairwise(nums):
        if a > b:
            shift = b + ceil((a - b) / 2)
            x = max(x, shift)

    if any((abs(a - x) > abs(b - x) for a, b in pairwise(nums))):
        print(-1)
    else:
        print(x)
