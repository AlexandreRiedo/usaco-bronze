import sys

NAMES = ["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"]

sys.stdin = open("lineup.in", "r")
sys.stdout = open("lineup.out", "w")

num_constraints = int(input())
constraints = []
for _ in range(num_constraints):
    cow_a, *_, cow_b = input().split()
    constraints.append((cow_a, cow_b))

valid_orderings = []


def verify(constraints, ordering):
    for idx, name in enumerate(ordering):
        for constraint in [
            constraint for constraint in constraints if name in constraint
        ]:
            other_cow = constraint[0] if constraint[0] != name else constraint[1]
            if (
                ordering[min(idx + 1, len(ordering) - 1)] != other_cow
                and ordering[max(idx - 1, 0)] != other_cow
            ):
                return False

    return True


ordering = []
used = [False for _ in range(len(NAMES))]


def solve(num_used: int = 0):
    if num_used == len(NAMES):
        if verify(constraints, ordering):
            valid_orderings.append(tuple(ordering))
        return

    for idx, name in enumerate(NAMES):
        if used[idx]:
            continue
        used[idx] = True
        ordering.append(name)
        solve(num_used + 1)
        ordering.pop()
        used[idx] = False


solve()
for cow in sorted(valid_orderings)[0]:
    print(cow)
