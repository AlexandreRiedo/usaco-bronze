from collections import Counter

num_cows = int(input())
cows = list(input())

left_G = cows.index("G")
left_H = cows.index("H")
right_G = len(cows) - list(reversed(cows)).index("G") - 1  # Inclusive
right_H = len(cows) - list(reversed(cows)).index("H") - 1  # Inclusive

count_cows = Counter(cows)

list_idx = [
    (start, end) for start, end in enumerate(map(lambda x: int(x) - 1, input().split()))
]  # Left is inclusive, Right is inclusive

G_leaders = set()
H_leaders = set()

for cow_idx, (left, right) in enumerate(list_idx):
    if cows[cow_idx] == "G":
        if left <= left_G and right >= right_G:
            G_leaders.add(cow_idx)
    elif cows[cow_idx] == "H":
        if left <= left_H and right >= right_H:
            H_leaders.add(cow_idx)

# CASE: all-breed leader + all_breed leader
count = len(G_leaders) * len(H_leaders)

# CASE: one all-breed + one that catches the other leader
for leader in range(num_cows):
    breed = cows[leader]

    if breed == "G":
        if leader not in G_leaders:
            count += len(
                set(range(list_idx[leader][0], list_idx[leader][1] + 1)) & H_leaders
            )
    elif breed == "H":
        if leader not in H_leaders:
            count += len(
                set(range(list_idx[leader][0], list_idx[leader][1] + 1)) & G_leaders
            )

print(count)

# from rich import print as rprint

# rprint(f"{cows=}")
# rprint(f"{count_cows=}")
# rprint(f"{list_idx=}")
# rprint(f"{left_G=} {left_H=} {right_G=} {right_H=}")
# rprint(f"{G_leaders=} {H_leaders=}")
# rprint(f"{count=}")
