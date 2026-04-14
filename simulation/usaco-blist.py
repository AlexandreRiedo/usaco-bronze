import sys

MAX_TIME = 1000

sys.stdin = open("blist.in", "r")
sys.stdout = open("blist.out", "w")

num_cows = int(input())
timeline = [0 for _ in range(MAX_TIME + 1)]
for _ in range(num_cows):
    s, t, b = map(int, input().split())
    for i in range(s, t+1):
        timeline[i] += b

print(max(timeline))