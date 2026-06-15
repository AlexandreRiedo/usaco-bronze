MODULO_SEARCH_UPPER_BOUND = 100

with open("swap.in") as f:
    num_cows, num_repeats = map(int, f.readline().split())
    a1, a2 = map(lambda x: int(x) - 1, f.readline().split())
    b1, b2 = map(lambda x: int(x) - 1, f.readline().split())


def solve(a1, b1, a2, b2, num_cows, num_repeats):
    order = list(range(1, num_cows + 1))

    for _ in range(num_repeats):
        order[a1 : a2 + 1] = reversed(order[a1 : a2 + 1])
        order[b1 : b2 + 1] = reversed(order[b1 : b2 + 1])

    return order


def find_modulo(a1, b1, a2, b2, num_cows):
    orderings = set()

    for num_repeats in range(0, MODULO_SEARCH_UPPER_BOUND + 1):
        ordering = tuple(solve(a1, b1, a2, b2, num_cows, num_repeats))

        if ordering in orderings:
            break
        else:
            orderings.add(ordering)

    return len(orderings)


with open("swap.out", "w") as f:
    modulo = find_modulo(a1, b1, a2, b2, num_cows)
    for item in solve(a1, b1, a2, b2, num_cows, num_repeats % modulo):
        f.write(f"{item}\n")
