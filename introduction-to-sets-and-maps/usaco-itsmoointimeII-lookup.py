from collections import defaultdict

n = int(input())
array = [int(x) for x in input().split()]

positions = defaultdict(list)
for i, x in enumerate(array):
    positions[x].append(i)

distinct_before = []
seen = set()
for x in array:
    distinct_before.append(len(seen))
    seen.add(x)

ans = 0
for ps in positions.values():
    if len(ps) >= 2:
        ans += distinct_before[ps[-2]]
        if len(ps) >= 3:
            ans -= 1
print(ans)