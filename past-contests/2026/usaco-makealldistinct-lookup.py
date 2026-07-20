T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    el = list(map(int, input().split()))
    moves = 0

    if K < 0:
        el = [num * -1 for num in el]
        K *= -1

    while el:
        m = min(el)
        new_el = []
        min_count = 0

        for num in el:
            if num == m:
                min_count += 1
            else:
                new_el.append(num)
        moves += min_count - 1

        for _ in range(min_count - 1):
            new_el.append(m + K)
        el = new_el

    print(moves)
