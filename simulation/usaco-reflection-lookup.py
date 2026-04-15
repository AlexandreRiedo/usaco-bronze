n, u = map(int, input().split())
grid = [list(input()) for _ in range(n)]


def contribution(r, c):
    cells = [
        grid[r][c],
        grid[n - r - 1][c],
        grid[r][n - c - 1],
        grid[n - r - 1][n - c - 1],
    ]
    painted = cells.count("#")
    return min(painted, 4 - painted)


ans = 0
for row in range(n // 2):
    for column in range(n // 2):
        ans += contribution(row, column)
print(ans)

for i in range(u):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    ans -= contribution(r, c)
    grid[r][c] = "#" if grid[r][c] == "." else "."
    ans += contribution(r, c)
    print(ans)
