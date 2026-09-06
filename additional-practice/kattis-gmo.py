apple = input()
swine = input()
costs = {["A", "C", "G", "T"][i]: int(v) for i, v in enumerate(input().split())}


def seq_cost(s):
    return sum(costs[c] for c in s)


def insert_cost(a: str, s: str, a_init: int):
    cost = seq_cost(s)
    s_idx = s.find(a[a_init])

    for a_char in a[a_init:]:
        if a_char not in s[s_idx:] or s_idx >= len(s) or s_idx == -1:
            break
        else:
            cost -= costs[a_char]
            s_idx += 1 + s[s_idx:].find(a_char)

    return cost


print(min(insert_cost(apple, swine, idx) for idx in range(len(apple))))

"""
GTA
CAT
A C G T
5 7 1 3
-> 10 (GTCAT)

TATA
CACA
A C G T
3 0 3 0
-> 3 (TCACATA or TATCACA)

TCGCGAG
TGCAG
A  C  G  T
10 10 15 15
-> 25 (TGCAG CGAG OR TCTGCAG)
"""
