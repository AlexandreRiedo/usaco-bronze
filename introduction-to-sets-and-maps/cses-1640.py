from collections import defaultdict

num_integers, target = map(int, input().split())
value_locations = defaultdict(list)
for idx, value in enumerate(input().split()):
    value_locations[str(value)].append(idx + 1)

idx_a = -1
idx_b = -1
for value_a in value_locations.keys():
    if (value_b := str(target - int(value_a))) in value_locations.keys():
        if value_a == value_b and len(value_locations[value_a]) == 1:
            continue

        idx_a = value_locations[value_a][0]
        idx_b = value_locations[value_b][-1]
        break

if idx_a == -1 and idx_b == -1:
    print("IMPOSSIBLE")
else:
    print(f"{idx_a} {idx_b}")
