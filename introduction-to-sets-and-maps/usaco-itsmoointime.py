import string
from collections import defaultdict

length, thresh = map(int, input().split())
contest = list(input())
moo_candidates = defaultdict(list)
moo_positions = defaultdict(set)
moos = set()

for idx in range(length - 2):
    first, second, third = contest[idx], contest[idx + 1], contest[idx + 2]

    if first != second and second == third:
        moo_candidates[f"{first}{second}{third}"].append(idx)

for moo, positions in moo_candidates.items():
    if len(positions) >= thresh:
        moos.add(moo)

    moo_positions[moo].update(pos + i for pos in positions for i in range(3))

for idx in range(length - 2):
    first, second, third = contest[idx], contest[idx + 1], contest[idx + 2]

    for letter in string.ascii_lowercase:
        for shift, potential in enumerate(
            (
                f"{letter}{second}{third}",
                f"{first}{letter}{third}",
                f"{first}{second}{letter}",
            )
        ):
            if potential[0] != potential[1] and potential[1] == potential[2]:
                if potential in moos:
                    continue
                elif idx + shift in moo_positions[potential]:
                    continue
                else:
                    if len(moo_candidates[potential]) + 1 >= thresh:
                        moos.add(potential)

print(len(moos))
for moo in sorted(moos):
    print(moo)
