from collections import defaultdict

length = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a_map = defaultdict(int)
for num in a:
    a_map[num] += 1

b_map = defaultdict(list)
for idx, num in enumerate(b):
    b_map[num].append(idx + 1)

c_map = defaultdict(list)
for idx, num in enumerate(c):
    c_map[num].append(idx + 1)

count = 0
for ai in a_map:
    if ai not in b_map:
        continue

    for pos in b_map[ai]:
        if pos not in c_map:
            continue
        else:
            count += len(c_map[pos]) * a_map[ai]

print(count)
