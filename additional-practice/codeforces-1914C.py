t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    points_a = list(map(int, input().split()))[:k]
    points_b = list(map(int, input().split()))[:k]

    score, curr_a_score, max_b = 0, 0, 0
    for idx, b in enumerate(points_b):
        curr_a_score += points_a[idx]
        remaining = k - (idx + 1)
        max_b = max(max_b, b)
        score = max(curr_a_score + max_b * remaining, score)

    print(score)