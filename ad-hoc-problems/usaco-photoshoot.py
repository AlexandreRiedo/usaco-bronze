N, K = map(int, input().split())
Q = int(input())

cows = [0 for _ in range(N)] * N
photos = [0 for _ in range(N - K + 1)] * (N - K + 1)
ans = 0

for _ in range(Q):
    r, c, v = (int(x) - 1 for x in input().split())

    if N >= 50:
        for y in range(max(0, r - K + 1), min(N - K, r) + 1):
            for x in range(max(0, c - K + 1), min(N - K, c) + 1):
                photos[x + y * (N - K + 1)] += v + 1 - cows[c + r * N]
                ans = max(photos[x + y * (N - K + 1)], ans)
        cows[c + r * N] = v + 1
        print(ans)
    else:
        for y in range(max(0, r - K + 1), min(N - K, r) + 1):
            for x in range(max(0, c - K + 1), min(N - K, c) + 1):
                photos[x + y * (N - K + 1)] += v + 1 - cows[c + r * N]
        cows[c + r * N] = v + 1
        print(max(photos))
