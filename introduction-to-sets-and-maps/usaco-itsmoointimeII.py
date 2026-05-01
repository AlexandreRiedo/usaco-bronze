from collections import defaultdict

len_nums = int(input())
nums = list(map(int, input().split()))

num_to_pos = defaultdict(list)
for idx, num in enumerate(nums):
    num_to_pos[num].append(idx)
dual_candidates = {key: value for key, value in num_to_pos.items() if len(value) >= 2}

candidates_dropout = sorted(value[-2] for value in dual_candidates.values())
candidates_count = [
    (len(dual_candidates) - i, candidates_dropout[i])
    for i in range(0, len(dual_candidates))
]
candidates_count.append((0, len_nums))

count = 0
candidates_count_idx = 0
for one_num, one_pos in num_to_pos.items():
    one_pos = one_pos[0]

    while candidates_count[candidates_count_idx][1] <= one_pos:
        candidates_count_idx += 1

    if candidates_count[candidates_count_idx][1] == len(nums):
        break

    duplicate = 0
    if (
        one_num in dual_candidates.keys()
        and dual_candidates[one_num][-2] > candidates_count[candidates_count_idx][1]
    ):
        duplicate -= 1
    if one_num == nums[candidates_count[candidates_count_idx][1]]:
        duplicate -= 1

    count += candidates_count[candidates_count_idx][0] + duplicate

print(count)