import sys

sys.stdin = open("paint.in", "r")
sys.stdout = open("paint.out", "w")

a, b = map(int, sys.stdin.readline().strip().split())
c, d = map(int, sys.stdin.readline().strip().split())

if a <= c <= b or a <= d <= b or c <= a <= d or c <= b <= d:
    sys.stdout.write(f"{max(a, b, c, d) - min(a, b, c, d)}")
else:
    sys.stdout.write(f"{(b - a) + (d - c)}")
