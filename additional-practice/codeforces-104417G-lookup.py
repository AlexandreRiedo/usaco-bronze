from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    seq = list(map(int, input().split()))
    ans = 0

    groups = defaultdict(list)
    for idx, num in enumerate(seq):
        groups[(idx + 1) - num].append(num)

    for group in groups.values():
        group.sort(reverse=True)
        for a, b in zip(group[::2], group[1::2]):
            if a + b > 0:
                ans += a + b

    print(ans)
