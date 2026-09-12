from bisect import bisect_right as br

N = int(input())
cows = sorted(map(int, input().split()))
stalls = sorted(map(int, input().split()))

pools = []
for h in stalls:
    pools.append(cows[: br(cows, h)])


def wrap(pools):
    global count
    count = 0

    def explore(used, pools):
        global count

        if len(used) == len(pools):
            count += 1
            return
        else:
            for cow in pools[len(used)]:
                if used.count(cow) == pools[len(used)].count(cow):
                    continue
                else:
                    used.append(cow)
                    explore(used, pools)
                    used.pop()

    explore([], pools)

    return count


# print(sum(all(c <= h for c, h in zip(o, stalls)) for o in permutations(cows, N)))
print(wrap(pools))

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
