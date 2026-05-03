from rich import print as rprint

n, _ = map(int, input().split())

inds = {}
arr = [int(i) for i in input().split()]
for i in range(n):
    if arr[i] not in inds:
        inds[arr[i]] = []
    inds[arr[i]].append(i)
rprint(f"{inds=}")

ranges = []
for i in inds.values():
    ranges.append((i[0], i[-1], len(i)))
ranges.sort()
rprint(f"{inds.values()=}")
rprint(f"{ranges=}")

difficulty = 0
start = ranges[0][0]
end = ranges[0][1]
most_common = 0
for r in ranges:
    if r[0] > end:
        difficulty += end - start + 1 - most_common
        start = r[0]
        end = r[1]
        most_common = r[2]
    else:
        end = max(end, r[1])
        most_common = max(most_common, r[2])
difficulty += end - start + 1 - most_common

print(difficulty)
