MODULO = 12

with open("swap.in") as f:
    num_cows, num_repeats = map(int, f.readline().split())
    a1, a2 = map(lambda x: int(x) - 1, f.readline().split())
    b1, b2 = map(lambda x: int(x) - 1, f.readline().split())


def solve(a1, b1, a2, b2, num_cows, num_repeats):
    order = list(range(1, num_cows + 1))

    for _ in range(num_repeats):
        # order[a1 : a2 + 1] = order[a2 : a1 - 1 : -1]
        # order[b1 : b2 + 1] = order[b2 : b1 - 1 : -1]
        order[a1 : a2 + 1] = reversed(order[a1 : a2 + 1])
        order[b1 : b2 + 1] = reversed(order[b1 : b2 + 1])

    return order


with open("swap.out", "w") as f:
    for item in solve(a1, b1, a2, b2, num_cows, num_repeats % MODULO):
        f.write(f"{item}\n")

# TESTING
# num_cows = random.randint(1, 100)
# a1, b1 = random.randint(1, num_cows - 1), random.randint(1, num_cows - 1)
# a2, b2 = random.randint(a1 + 1, num_cows), random.randint(b1 + 1, num_cows)

# rprint(f"{num_cows=} {a1=} {a2=} {b1=} {b2=}\n\n")

# orderings = set()
# ordering_to_num_repeats = defaultdict(int)

# for num_repeats in range(1, num_cows + 1):
#     ordering = tuple(solve(a1, b1, a2, b2, num_cows, num_repeats))

#     if ordering in orderings:
#         continue
#         rprint(f"{ordering=} with {num_repeats=} already seen in num_repeats={ordering_to_num_repeats[ordering]}")
#     else:
#         orderings.add(ordering)
#         ordering_to_num_repeats[ordering] = num_repeats

# rprint(f"\n{orderings=}")
# rprint(f"cycle length: {max(ordering_to_num_repeats.values())}")
