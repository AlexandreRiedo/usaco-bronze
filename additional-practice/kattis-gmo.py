a = input()
s = input()
costs = {["A", "C", "G", "T"][i]: int(v) for i, v in enumerate(input().split())}


def seq_cost(s):
    return sum(costs[c] for c in s)


def insert_cost(a: str, s: str, a_init: int, cost: int, init_find: dict[str, int]):
    s_idx = init_find[a[a_init]]

    for a_char in a[a_init:]:
        if a_char not in s[s_idx:] or s_idx >= len(s) or s_idx == -1:
            break
        else:
            cost -= costs[a_char]
            s_idx += 1 + s[s_idx:].find(a_char)

    return cost


f = {c: s.find(c) for c in ["A", "C", "G", "T"]}
cost = seq_cost(s)
print(min(insert_cost(a, s, idx, cost, f) for idx in range(len(a))))
