N = int(input())
order = list(map(int, input().split()))
goal = list(map(int, input().split()))

swap = 0
swapped = set()
for idx in range(N):
    if order[idx] != goal[idx]:
        order[idx:] = [goal[idx]] + [x for x in order[idx:] if x != goal[idx]]
        swap += 1

print(swap)
