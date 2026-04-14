import sys

sys.stdin = open("teleport.in", "r")
sys.stdout = open("teleport.out", "w")

a, b, x, y = map(int, input().split())

a, b = min(a, b), max(a, b)
x, y = min(x, y), max(x, y)

if (abs(a - x) + abs(b - y)) < (b - a):
    print(f"{abs(a - x) + abs(b - y)}")
else:
    print(f"{b - a}")
