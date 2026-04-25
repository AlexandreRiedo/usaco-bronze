num_apples = int(input())
weights = list(map(int, input().split()))


def solve(a, b, idx):
    if idx == num_apples:
        return abs(a - b)

    return min(
        solve(a + weights[idx], b, idx + 1),
        solve(a, b + weights[idx], idx + 1),
    )


print(solve(0, 0, 0))
