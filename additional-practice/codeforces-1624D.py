from collections import Counter

from rich import print as rprint

for _ in range(int(input())):
    _, k = map(int, input().split())
    s = input()
    chars = Counter(s)
    rprint(f"{chars=}")
    rprint("")

"""
10
8 2
bxyaxzay
-> axybyzax
-> axybyax
-> aba xyyx
-> 3

6 3
aaaaaa
-> aa aa aa
-> 2

6 1
abcdef
-> a/b/c/d/e/f
-> 1

6 6
abcdef
-> a b c d e f
-> 1

3 2
dxd
-> dd x
-> 1

11 2
abcabcabcac
-> abcab cabac c
-> abcba acbca c
-> 5
OR
-> aabaa ccbcc b

6 6
sipkic
-> s i p k i c
-> 1

7 2
eatoohd
-> e oao thd
-> 1

3 1
llw
-> lwl
-> 3

6 2
bfvfbv
-> fbf vbv
-> 3
"""
