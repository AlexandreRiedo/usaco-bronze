with open("swap.in") as f:
    num_cows, num_repeats = map(int, f.readline().split())
    a1, a2 = map(lambda x: int(x) - 1, f.readline().split())
    b1, b2 = map(lambda x: int(x) - 1, f.readline().split())


def step(a1, b1, a2, b2, order):
    new_order = order.copy()

    new_order[a1 : a2 + 1] = reversed(new_order[a1 : a2 + 1])
    new_order[b1 : b2 + 1] = reversed(new_order[b1 : b2 + 1])

    return new_order


def find_modulo(a1, b1, a2, b2, num_cows):
    init_order = list(range(1, num_cows + 1))
    curr_order = step(a1, b1, a2, b2, init_order)
    modulo = 1

    while init_order != curr_order:
        curr_order = step(a1, b1, a2, b2, curr_order)
        modulo += 1

    return modulo


def solve(a1, b1, a2, b2, num_cows, num_repeats):
    order = list(range(1, num_cows + 1))

    for _ in range(num_repeats):
        order = step(a1, b1, a2, b2, order)

    return order


with open("swap.out", "w") as f:
    modulo = find_modulo(a1, b1, a2, b2, num_cows)
    for item in solve(a1, b1, a2, b2, num_cows, num_repeats % modulo):
        f.write(f"{item}\n")
