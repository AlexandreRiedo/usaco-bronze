import itertools


def count(groups: list[list[str]]):
    ans = 0
    alt_ans = 0

    # Case : try to remove the smallest "A" group and see if that works
    if len(groups) % 2 == 1:
        to_remove = min([x for x in groups if x != ["B"]], default=None)
        if to_remove is not None:
            alt_groups = groups[:]
            alt_groups.remove(to_remove)
            while len(alt_groups) >= 2:
                if {"A", "B"}.issubset({*alt_groups[-1], *alt_groups[-2]}):
                    alt_ans += alt_groups.pop().count("A") + alt_groups.pop().count("A")
                else:
                    alt_groups.pop()

    # The default calculation
    while len(groups) >= 2:
        if {"A", "B"}.issubset({*groups[-1], *groups[-2]}):
            ans += groups.pop().count("A") + groups.pop().count("A")
        else:
            groups.pop()

    return max(ans, alt_ans)


def solve(s) -> int:
    groups = []

    for _, group in itertools.groupby(s):
        group = list(group)
        if group.count("B") > 1:
            groups.extend((["B"], ["B"]))
        else:
            groups.append(group)

    return max(count(groups[:]), count(list(reversed(groups[:]))))


for _ in range(int(input())):
    s = list(input())
    print(solve(s))
