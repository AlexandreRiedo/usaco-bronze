num_cows = int(input())
farmer_order = [int(item) - 1 for item in input().split()]
vet_order = [int(item) - 1 for item in input().split()]


def count_checked(proposed_order, vet_order):
    count = 0
    for a, b in zip(proposed_order, vet_order):
        if a == b:
            count += 1
    return count


checked_count = {i: 0 for i in range(num_cows + 1)}
for left in range(num_cows):
    for right in range(left + 1, num_cows + 1):
        checked_count[
            count_checked(
                farmer_order[:left]
                + list(reversed(farmer_order[left:right]))
                + farmer_order[right:],
                vet_order,
            )
        ] += 1

for checked, count in sorted(checked_count.items(), key=lambda kv: kv[0]):
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
