num_cows = int(input())
farmer_order = [int(item) - 1 for item in input().split()]
vet_order = [int(item) - 1 for item in input().split()]


def count_checked(proposed_order, vet_order, left, right):
    count = 0
    if proposed_order[left] == vet_order[right]:
        count += 1
    if proposed_order[right] == vet_order[left]:
        count += 1
    return count


def build_left_checked(farmer_order, vet_order, num_cows):
    checked_left = [0 for _ in range(num_cows)]
    for index, (farmer_cow, vet_cow) in enumerate(zip(farmer_order, vet_order)):
        if index != 0:
            checked_left[index] = checked_left[index - 1]
        if farmer_cow == vet_cow:
            checked_left[index] += 1
    return checked_left


def build_right_checked(farmer_order, vet_order, num_cows):
    checked_right = [0 for _ in range(num_cows)]
    for index, (farmer_cow, vet_cow) in enumerate(
        zip(reversed(farmer_order), reversed(vet_order))
    ):
        if index != 0:
            checked_right[index] = checked_right[index - 1]
        if farmer_cow == vet_cow:
            checked_right[index] += 1
    checked_right.reverse()
    return checked_right


def get_expansion_tuples(values, index, offset):
    left = index
    right = index + offset
    tuples_found = [(left - 1, right - 1)]
    expansion = 0
    while left - expansion > 1 and right + expansion <= len(values) - 1:
        expansion += 1
        tuples_found.append((left - 1 - expansion, right - 1 + expansion))
    return tuples_found


checked_left = [0] + build_left_checked(farmer_order, vet_order, num_cows)
checked_right = build_right_checked(farmer_order, vet_order, num_cows) + [0]
checked_count = {i: 0 for i in range(num_cows + 1)}

calculations = 1

for offset in (0, 1):
    for i in range(1, num_cows):
        prev_result = 0
        result = 0
        for left, right in get_expansion_tuples(farmer_order, i, offset):
            calculations += 1
            if left == right:
                to_add = 0 if farmer_order[left] != vet_order[left] else 1
            else:
                to_add = count_checked(farmer_order, vet_order, left, right)

            result = (
                to_add + prev_result + checked_left[left] + checked_right[right + 1]
            )
            prev_result += to_add

            checked_count[result] += 1


checked_count[checked_left[num_cows - 1] + checked_right[num_cows - 1]] += 1

for _, count in sorted(checked_count.items(), key=lambda kv: kv[0]):
    print(count)

from rich import print as rprint

rprint(f"{calculations=}")