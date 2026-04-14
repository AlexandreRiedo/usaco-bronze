import sys

sys.stdin = open("cowsignal.in", "r")
sys.stdout = open("cowsignal.out", "w")

M, N, K = map(int, input().split())
grid = []
for _ in range(M):
    row = []
    for char in input():
        row.append(char)
    grid.append(row)

new_grid = []
for row in grid:
    new_row = []
    for index, char in enumerate(row):
        for _ in range(K):
            new_row.append(char)
    for _ in range(K):
        new_grid.append(new_row)

for row in new_grid:
    print("".join(row))
