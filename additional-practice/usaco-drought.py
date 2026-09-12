for _ in range(int(input())):
    N = int(input())
    h = list(map(int, input().split()))
    h_og = h.copy()

    for i in range(len(h)):
        if i == len(h) - 1:
            continue
        elif i == len(h) - 2:
            if h[i] < h[i + 1] or (len(h) % 2 == 0 and h[i] != h[i + 1]):
                print(-1)
                break
            else:
                h[: i + 1] = [h[i + 1]] * (i + 1)
        else:
            if h[i + 1] > h[i]:
                d = h[i + 1] - h[i]
                h[i + 1] -= d
                h[i + 2] -= d
                if h[i + 2] < 0:
                    print(-1)
                    break
            elif h[i + 1] < h[i]:
                if i % 2 == 0:
                    print(-1)
                    break
                else:
                    h[: i + 1] = [h[i + 1]] * (i + 1)
    else:
        print(sum(a - b for a, b in zip(h_og, h)))
