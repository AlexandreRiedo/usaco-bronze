from bisect import bisect_right
from collections import defaultdict

n = int(input())
nums = list(map(int, input().split()))

# For each value, the sorted indices where it appears.
positions = defaultdict(list)
for i, x in enumerate(nums):
    positions[x].append(i)

# A value is a "duplicate" if it appears >= 2 times. Its second-to-last
# index is the "dropout": past it, fewer than 2 occurrences remain.
duplicates = {x: ps for x, ps in positions.items() if len(ps) >= 2}
dropouts = sorted(ps[-2] for ps in duplicates.values())

total = 0
for x, ps in positions.items():
    first = ps[0]

    # How many distinct values still have >= 2 occurrences after `first`?
    next_idx = bisect_right(dropouts, first)
    remaining = len(dropouts) - next_idx
    if remaining == 0:
        continue

    # Don't count x itself when it's one of those remaining duplicates.
    if x in duplicates and duplicates[x][-2] > first:
        remaining -= 1

    # Don't count the value whose dropout is the very next one above `first`.
    if nums[dropouts[next_idx]] == x:
        remaining -= 1

    total += remaining

print(total)