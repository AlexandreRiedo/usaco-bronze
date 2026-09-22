N, K = map(int, input().split())
cows = [[0 for _ in range(N)] for _ in range(N)]
Q = int(input())

for _ in range(Q):
    r, c, v = (int(x) - 1 for x in input().split())
    cows[r][c] = v + 1

    ans = 0
    for y in range(max(0, N - K + 1)):
        for x in range(max(0, N - K + 1)):
            curr = 0
            for r in range(x, x + K):
                for c in range(y, y + K):
                    curr += cows[r][c]
            ans = max(curr, ans)

    print(ans)

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
0   0   0
0   0   3

0   0   0
0   0   0
0   0   5

0   0   0
0   0   0
0   0   7
"""
