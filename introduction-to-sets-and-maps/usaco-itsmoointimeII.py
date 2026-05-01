from collections import defaultdict

_ = int(input())
nums = list(map(int, input().split()))

num_to_pos = defaultdict(list)
for idx, num in enumerate(nums):
    num_to_pos[num].append(idx)
dual_candidates = {key: value for key, value in num_to_pos.items() if len(value) >= 2}

# rprint(f"{num_to_pos}")
# rprint(f"{dual_candidates=}")

count = 0
for one_num, one_pos in num_to_pos.items():
    one_pos = one_pos[0]
    # rprint(f"{one_num=} {one_pos=}")

    for dual_num, dual_positions in dual_candidates.items():
        if dual_num == one_num:
            continue

        if dual_positions[-2] > one_pos:
            count += 1

print(count)

"""
[4, 6, 4, 6, 7, 6, 2, 6, 6, 8, 10, 7, 3, 4, 10, 7, 6, 2, 9, 3, 4, 7, 9, 3, 5]
25
4 6 4 6 7 6 2 6 6 8 10 7 3 4 10 7 6 2 9 3 4 7 9 3 5
"""

"""
[1, 9, 10, 10, 2, 6, 1, 6, 10, 2]
10
1 9 10 10 2 6 1 6 10 2

1 10 10
1 2 2
1 6 6

9 10 10
9 2 2
9 6 6

10 2 2
10 6 6

2 6 6
"""
