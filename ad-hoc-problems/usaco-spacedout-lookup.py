N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
max_rows, max_cols = 0, 0

for i in range(N):
    max_rows += max(sum(grid[i][::2]), sum(grid[i][1::2]))
    max_cols += max(
        sum(grid[l][i] for l in range(0, N, 2)),
        sum(grid[l][i] for l in range(1, N, 2)),
    )

print(max(max_rows, max_cols))
