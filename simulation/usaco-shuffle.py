import sys

NUM_SHUFFLES = 3

sys.stdin = open("shuffle.in", "r")
sys.stdout = open("shuffle.out", "w")

n = int(input())
shuffle = [int(item) - 1 for item in input().split()]
order = [int(item) for item in input().split()]
new_order = list(range(n))

for _ in range(NUM_SHUFFLES):
    for index, shuffle_move in enumerate(shuffle):
        new_order[index] = order[shuffle_move]
    order[:] = new_order

for id in order:
    print(id)    