import itertools

k, n = map(int, input().split())
marks = list(map(int, input().split()))
remembered = list(map(int, input().split()))
prefix = list(itertools.accumulate(marks))

valid = set()
for idx, points in enumerate(remembered):
    curr_set = set()
    for calculation in prefix:
        curr_set.add(points - calculation)

    if idx == 0:
        valid = curr_set
    else:
        valid = valid.intersection(curr_set)

print(len(valid))
