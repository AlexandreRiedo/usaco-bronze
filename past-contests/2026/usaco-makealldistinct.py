from collections import Counter

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    el = list(map(int, input().split()))
    el_counter = Counter(el)
    moves = 0

    while max(el_counter.values()) > 1:
        el_sorted = sorted(el_counter.keys(), reverse=K < 0)
        for num in el_sorted:
            if el_counter[num] <= 1:
                continue
            else:
                moves += (el_counter[num] - 1) * (el_counter[num]) // 2
                for n in range(1, el_counter[num]):
                    el_counter[num + (n * K)] += 1
                el_counter[num] -= el_counter[num] - 1

    print(moves)

"""
4 1 4 1
5 1 4 1
5 1 4 2 -> 2

4 1 4 1
1 1 4 1
1 -2 4 1
-2 -2 4 1
-4 -2 4 1 -> 4

4 1 4 1
8 1 4 1
8 5 4 1 -> 2

1 1 2
-1 1 2 -> 1
"""

"""
import random
VAL=6
print(f"{VAL} {random.randint(-VAL, VAL)}")
print(*[random.randint(1,VAL) for _ in range(VAL)], sep=" ")
"""

"""
6 -3
3 3 6 1 6 3
0 3 6 1 6 3
0 0 6 1 6 3
-3 0 6 1 6 3
-3 0 6 1 3 3
-3 0 6 1 0 3
-3 0 6 1 -3 3
-6 0 6 1 -3 3 -> 7
For the 3s to be unique: 1+2
For the 6s to be unique: 1 + 3

6 -5
4 3 1 2 2 2
4 3 1 2 2 -3
4 3 1 2 -3 -3
4 3 1 2 -3 -8 -> 3
For the 2s to be unique: 1+2

6 -1
6 6 6 6 6 6
6 5 5 5 5 5 (x5)
6 5 4 4 4 4 (x4)
6 5 4 3 3 3 (x3)
6 5 4 3 2 2 (x2)
6 5 4 3 2 1 (x1) -> 15
For the 6s to be unique: 5+4+3+2+1=15

6 -1
6 4 2 1 6 2
6 4 2 1 5 2
6 4 2 1 5 1
6 4 2 0 5 1 -> 3
For the 6s to be unique: 1
For the 2s to be unique: 1+2

6 1
5 1 4 4 6 3
5 1 4 5 6 3
6 1 4 5 6 3
7 1 4 5 6 3 -> 3


6 5
5 6 3 4 2 3
5 6 8 4 2 3 -> 1
"""

"""
10 9
2 1 4 2 1 1 10 10 7 7

"""
