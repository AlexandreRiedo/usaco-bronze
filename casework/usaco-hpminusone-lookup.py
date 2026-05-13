num_symbols, num_games = map(int, input().split())
beatenBy = [[False for _ in range(num_symbols)] for _ in range(num_symbols)]
for i in range(0, num_symbols):
    data = input()
    for j in range(0, i + 1):
        state = data[j]
        if state == "L":
            beatenBy[i][j] = True
        elif state == "W":
            beatenBy[j][i] = True

# STRATEGY 1
# for _ in range(num_games):
#     l, r = map(lambda x: int(x) - 1, input().split())  # noqa: E741
#     possible = 0
#     for myL in range(0, num_symbols):
#         for myR in range(0, num_symbols):
#             if (beatenBy[l][myL] and beatenBy[r][myL]) or (
#                 beatenBy[l][myR] and beatenBy[r][myR]
#             ):
#                 possible += 1
#     rprint(possible)

# STRATEGY 2
for _ in range(num_games):
    l, r = map(lambda x: int(x) - 1, input().split())  # noqa: E741
    x = sum(1 for g in range(num_symbols) if beatenBy[l][g] and beatenBy[r][g])
    possible = x * num_symbols + x * (num_symbols - x)
    print(possible)
