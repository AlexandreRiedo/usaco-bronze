from collections import Counter
from itertools import combinations

nums = [int(item) for item in input().split()]

for a_index, b_index, c_index in combinations(range(7), 3):
    other_nums = Counter(
        [
            num
            for index, num in enumerate(nums)
            if index not in (a_index, b_index, c_index)
        ]
    )
    a = nums[a_index]
    b = nums[b_index]
    c = nums[c_index]

    if Counter([a + b + c, a + b, b + c, c + a]) == other_nums:
        print(" ".join(map(str, sorted([a, b, c]))))
