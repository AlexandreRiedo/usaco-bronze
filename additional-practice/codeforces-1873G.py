import itertools


def count(groups):
    ans = 0
    while len(groups) >= 2:
        if {"A", "B"}.issubset({*groups[-1], *groups[-2]}):
            ans += groups.pop().count("A") + groups.pop().count("A")
        else:
            groups.pop()
    return ans


def solve(s) -> int:
    groups = []

    for _, group in itertools.groupby(s):
        group = list(group)
        if group.count("B") > 1:
            groups.extend((["B"], ["B"]))
        else:
            groups.append(group)

    return max(count(groups[:]), count(list(reversed(groups[:]))))


# for _ in range(int(input())):
#     s = list(input())
#     print(solve(s))

import random

from rich import print as rprint

while (s := "".join([random.choice("AB") for _ in range(10)])).count("A") == solve(s):
    continue
rprint(f"{s=} {solve(s)=}")

"""
V2 COUNTER EXAMPLE
AAAAABABAA
-> code gives 6
-> AAAAAB BAA gives 7
"""

"""
AAABABAABA
-> BA BAA BA with 4
-> AAAB AB AAB with 6
"""

"""
ABABAABABBBBBABABABABAABA
A B A B AA B A B    B A B A B A B A B AA B A
AB AB AAB AB    BA BA BA BA BAA BA -> 
BA BAA BA BA    BA BA BA BAA BA
"""

"""
VIP: COUNTER-EXAMPLE OF MY IDEA
ABAABAABBA
BAA BAA BA
-> ACCBCCBBCB with 5

AB AAB AAB BA
-> BC BCC BCC CB with 6
---
VIP: COUNTER-EXAMPLE 2
ABAAB
-> ACCBB with 2
-> BCBCC with 3
---
ABAABAAAB
"""

"""
A B AA B AA B B A
-> AB AAB AAB BA
-> BAA BAA BA
"""

"""
---
BAABA
CBABA
CCBBA
CCBCB -> 3

BAABA
BABCA
BBCCA -> 2
---
BABA
CBBA
CBCB -> 2

BABA
BBCA -> 1
---
BAAAAB
CBAAAB
CCBAAB
CCCBAB
CCCCBB -> 4

BAAAAB
BAAABC
BAABCC
BABCCC
BBCCCC -> 4
---
AABAAAA
AACBAAA
AACCBAA
AACCCBA
AAACCCB -> 4

AABAAAA
ABCAAAA
BCCAAAA -> 2
---
BABAABB
CBBAABB
CBCBABB
CBCCBBB -> 3
---
BBABA

"""

"""
"".join([random.choice("AB") for _ in range(25)])
"""
