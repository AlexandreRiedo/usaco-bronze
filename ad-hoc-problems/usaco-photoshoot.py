N, K = map(int, input().split())
Q = int(input())

cows = [[0 for _ in range(N)] for _ in range(N)]
photos = [0 for _ in range(N - K + 1)] * (N - K + 1)
ans = 0

for _ in range(Q):
    r, c, v = (int(x) - 1 for x in input().split())

    # Crazy ass hack to get 12/18
    if N > 50:
        for y in range(max(0, r - K + 1), min(N - K, r) + 1):
            for x in range(max(0, c - K + 1), min(N - K, c) + 1):
                photos[x + y * (N - K + 1)] += v + 1 - cows[r][c]
                ans = max(photos[x + y * (N - K + 1)], ans)
        cows[r][c] = v + 1
        print(ans)
    else:
        for y in range(max(0, r - K + 1), min(N - K, r) + 1):
            for x in range(max(0, c - K + 1), min(N - K, c) + 1):
                photos[x + y * (N - K + 1)] += v + 1 - cows[r][c]
        cows[r][c] = v + 1
        print(max(photos))

# N, K = map(int, input().split())
# Q = int(input())

# cows = [[0 for _ in range(N)] for _ in range(N)]
# photos = [0 for _ in range(N - K + 1)] * (N - K + 1)

# for _ in range(Q):
#     r, c, v = (int(x) - 1 for x in input().split())

#     for y in range(max(0, r - K + 1), min(N - K, r) + 1):
#         for x in range(max(0, c - K + 1), min(N - K, c) + 1):
#             photos[x + y * (N - K + 1)] += v + 1 - cows[r][c]
#     cows[r][c] = v + 1

#     print(max(photos))
