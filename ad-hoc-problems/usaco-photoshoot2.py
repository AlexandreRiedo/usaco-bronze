N = int(input())
order = list(map(int, input().split()))
goal = list(map(int, input().split()))

swap = 0

for idx in range(N):
    if order[idx] != goal[idx]:
        order[idx:] = [goal[idx]] + [x for x in order[idx:] if x != goal[idx]]
        swap += 1

print(swap)

"""
5 1 3 2 4
^
4 5 2 1 3
^

5 1 3 2 4
^
4 5 2 1 3
  ^
moved = 5

5 1 3 2 4
  ^
4 5 2 1 3
    ^
moved = 5,2

5 1 3 2 4
    ^
4 5 2 1 3
      ^
moved = 5,2

5 1 3 2 4
      ^
4 5 2 1 3
        ^
moved = 5,2
"""