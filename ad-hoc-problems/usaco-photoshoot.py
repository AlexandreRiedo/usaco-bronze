N, K = map(int, input().split())
Q = int(input())

cows = [[0 for _ in range(N)] for _ in range(N)]
photos = [0 for _ in range(N - K + 1)] * (N - K + 1)

for _ in range(Q):
    r, c, v = (int(x) - 1 for x in input().split())

    for y in range(max(0, r - K + 1), min(N - K, r) + 1):
        for x in range(max(0, c - K + 1), min(N - K, c) + 1):
            photos[x + y * (N - K + 1)] += v + 1 - cows[r][c]
    cows[r][c] = v + 1

    print(max(photos))


"""
4 2
3
2 2 11
3 4 3
3 1 100

0000
0000
0000
0000

0  0  0  0
0  11 0  0
0  0  0  0
0  0  0  0

0  0  0  0
0  11 0  0
0  0  0  3
0  0  0  0

0   0   0   0
0   11  0   0
100 0   0   3
0   0   0   0
"""

"""
3 1
3
2 2 3
2 2 5
2 2 7

0   0   0
0   0   0
0   0   0

0   0   0
0   3   0
0   0   0

0   0   0
0   5   0
0   0   0

0   0   0
0   7   0
0   0   0
"""
