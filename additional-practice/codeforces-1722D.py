from itertools import pairwise
from math import ceil

from rich import print as rprint

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    x = 0

    for a, b in pairwise(nums):
        a, b = abs(a - x), abs(b - x)

        if b < a:
            x = b + ceil((a - b) / 2)

        rprint(f"{a=} {b=} {x=} {abs(a - x)=} {abs(b - x)=}")
    rprint()

"""
5 3 3 3 5

x=4:
5-4 = 1
3-4 = -1 = 1
3-4 = -1 = 1
3-4 = -1 = 1
5-4 = 1

x=5:
5-5 = 0
3-5 = -2 = 2
3-5 = -2 = 2
3-5 = -2 = 2
5-5 = 0

"""
