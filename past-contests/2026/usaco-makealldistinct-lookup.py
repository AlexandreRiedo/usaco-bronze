from collections import defaultdict

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    cnt_at = defaultdict(int)
    for num in [int(x) - 1 for x in input().split()]:
        cnt_at[num] += 1

    moves = 0
    cur_min = 0
    cnt_min = 0
    while cur_min < N or cnt_min > 0:
        if cur_min < N:
            cnt_min += cnt_at[cur_min]
        if cnt_min > 0:
            moves += cnt_min - 1
            cnt_min -= 1
        cur_min += 1

    print(moves)
