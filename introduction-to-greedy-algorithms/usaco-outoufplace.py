from collections import defaultdict

with open("outofplace.in") as f:
    num_cows = int(f.readline().strip())
    cows = [int(f.readline().strip()) for _ in range(num_cows)]

sorted_cows = sorted(cows)
cow_to_idx = defaultdict(list)
for idx, cow in enumerate(sorted_cows):
    cow_to_idx[cow].append(idx)

res = 0
for (idx_a, cow_a), (idx_b, cow_b) in zip(enumerate(cows), enumerate(cows[1:], 1)):
    if cow_b < cow_a:
        a_left, a_right = (
            min(idx_a, min(cow_to_idx[cow_a])),
            max(idx_a, max(cow_to_idx[cow_a])),
        )
        b_left, b_right = (
            min(idx_b, min(cow_to_idx[cow_b])),
            max(idx_b, max(cow_to_idx[cow_b])),
        )
        a_dist = len(set(sorted_cows[a_left:a_right]) - {cow_a})
        b_dist = len(set(sorted_cows[b_left:b_right]) - {cow_b})
        res = max(a_dist + 1, b_dist + 1, 0)

        if a_dist == 0 and b_dist == 0:
            res = 0

with open("outofplace.out", "w") as f:
    f.write(f"{res}\n")

"""
2 4 7 7 9 3

2 4 3 7 7 9 

2 3 4 9 7 7
"""
