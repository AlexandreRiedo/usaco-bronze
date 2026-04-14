import sys

sys.stdin = open("shell.in", "r")
sys.stdout = open("shell.out", "w")

n = int(input())
swaps = []
for _ in range(n):
    a, b, g = map(int, input().split())
    swaps.append((a, b, g))

best = 0
for location in range(1, 4):
    correct = 0
    for a, b, g in swaps:
        if location == a:
            location = b
        elif location == b:
            location = a

        if location == g:
            correct += 1

    best = max(best, correct)
print(best)
