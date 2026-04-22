num_cows = int(input())
farmer_order = [int(item) - 1 for item in input().split()]
vet_order = [int(item) - 1 for item in input().split()]


def count_checked(proposed_order, vet_order):
    count = 0
    for a, b in zip(proposed_order, vet_order):
        if a == b:
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


checked_left = [0] + build_left_checked(farmer_order, vet_order, num_cows)
checked_right = build_right_checked(farmer_order, vet_order, num_cows) + [0]

checked_count = {i: 0 for i in range(num_cows + 1)}
for left in range(num_cows):
    for right in range(left + 1, num_cows + 1):
        checked_count[
            count_checked(
                list(reversed(farmer_order[left:right])),
                vet_order[left:right],
            )
            + checked_left[left]
            + checked_right[right]
        ] += 1

for _, count in sorted(checked_count.items(), key=lambda kv: kv[0]):
    print(count)

"""
3
1 3 2
3 2 1

7
1 3 2 2 1 3 2
3 2 2 1 2 3 1
1 3 2 1 2 3 2 (l4 r5)
1 3 2 2 2 3 1 (l5 r7)

7
1 3 2 2 1 3 2
3 2 2 1 2 3 1


2 3 1 2 1 3 2 (l1 r3)
1 3 2 2 3 1 2 (l4 r7)
1 2 3 2 1 3 2 (l2 r3)
1 3 2 2 1 2 3 (l6 r7)



"""
