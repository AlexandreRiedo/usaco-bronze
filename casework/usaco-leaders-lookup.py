num_cows = int(input())
cows = list(input())

left_G = cows.index("G")
left_H = cows.index("H")
right_G = len(cows) - list(reversed(cows)).index("G") - 1  # Inclusive
right_H = len(cows) - list(reversed(cows)).index("H") - 1  # Inclusive

list_idx = [
    (start, end) for start, end in enumerate(map(lambda x: int(x) - 1, input().split()))
]  # Left is inclusive, Right is inclusive

G_leader = None
H_leader = None

left, right = list_idx[left_G]
if left <= left_G and right >= right_G:
    G_leader = left_G

left, right = list_idx[left_H]
if left <= left_H and right >= right_H:
    H_leader = left_H

count = 0 if G_leader is None or H_leader is None else 1

for other_leader, other_leader_char in enumerate(cows):
    if other_leader == G_leader or other_leader == H_leader:
        continue

    left, right = list_idx[other_leader]

    if other_leader_char == "G" and H_leader is not None:
        if left <= H_leader and right >= H_leader:
            count += 1

    if other_leader_char == "H" and G_leader is not None:
        if left <= G_leader and right >= G_leader:
            count += 1

print(count)
