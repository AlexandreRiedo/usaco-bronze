def prod(a):
    ans = a[0]
    for num in a[1:]:
        ans *= num
    return ans


N = int(input())
cows = sorted(map(int, input().split()), reverse=True)
stalls = sorted(map(int, input().split()))

ans = []
for idx, c in enumerate(cows):
    ans.append(sum(c <= h for h in stalls) - idx)
print(prod(ans))


# print(sum(all(c <= h for c, h in zip(o, stalls)) for o in permutations(cows, N)))
# rprint(*[o for o in permutations(cows, N) if all(c <= h for c, h in zip(o, stalls))])

"""
[(1,2), (1,2,3), (1,2,3,4), (1,2,3,4)]

4
1 2 3 4
2 3 4 4
-> 8
1 2 3 4
1 2 4 3
1 3 2 4
1 3 4 2
2 1 3 4
2 1 4 3
2 3 1 4
2 3 4 1

4
1 2 3 4
2 3 3 4
-> 4
1 2 3 4
1 3 2 4
2 1 3 4
2 3 1 4
"""

"""
(1, 2, 3, 4)
(1, 2, 4, 3)
(1, 3, 2, 4)
(1, 3, 4, 2)
(1, 4, 2, 3)
(1, 4, 3, 2)
(2, 1, 3, 4)
(2, 1, 4, 3)
(2, 3, 1, 4)
(2, 3, 4, 1)
(2, 4, 1, 3)
(2, 4, 3, 1)
(3, 1, 2, 4)
(3, 1, 4, 2)
(3, 2, 1, 4)
(3, 2, 4, 1)
(3, 4, 1, 2)
(3, 4, 2, 1)
(4, 1, 2, 3)
(4, 1, 3, 2)
(4, 2, 1, 3)
(4, 2, 3, 1)
(4, 3, 1, 2)
(4, 3, 2, 1)
"""
