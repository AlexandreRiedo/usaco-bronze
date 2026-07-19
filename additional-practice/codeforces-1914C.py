t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    points_a = list(map(int, input().split()))[:k]
    points_b = list(map(int, input().split()))[:k]

    score = 0
    for idx_b, b in enumerate(points_b):
        curr_score = sum(points_a[: idx_b + 1])
        remaining = k - (idx_b + 1)
        max_b = max(points_b[: idx_b + 1])

        curr_score += max_b * remaining
        score = max(curr_score, score)

    print(score)

"""
1
4 7
4 3 1 2
1 1 1 1
-> 4 + 3 + 1 + 2 + 1 + 1 + 1

1
5 5
3 2 4 1 4
2 3 1 4 7
-> 3 + 2 + 4 + 3 + 3

1
6 4
1 4 5 4 5 10
1 5 1 2 5 1
-> 1 + 4 + 5 + 5
"""
