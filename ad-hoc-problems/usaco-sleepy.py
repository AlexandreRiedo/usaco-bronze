def is_monotonic_inc(seq):
    return all(seq[i] < seq[i + 1] for i in range(len(seq) - 1))


def last_monotonic_inc_idx(seq):
    idx = len(seq) - 1
    while idx > 0 and seq[idx - 1] < seq[idx]:
        idx -= 1
    return idx


def greedy_insertion_idx(seq, idx):
    while idx < len(seq) and seq[idx] < seq[0]:
        idx += 1
    return idx


with open("sleepy.in") as f:
    N = int(f.readline())
    order = list(map(int, f.readline().split()))

steps = 0
while not is_monotonic_inc(order):
    steps += 1
    order.insert(greedy_insertion_idx(order, last_monotonic_inc_idx(order)), order[0])
    order.pop(0)

with open("sleepy.out", "w") as f:
    f.write(f"{steps}\n")


"""
# IDEA: Find the right most monotonic sequence, insert at the greediest position
"""

"""
1 2 4 3
2 4 1 3
4 1 2 3
1 2 3 4 -> 3 moves
"""

"""
3 4 5 1 2
4 5 1 2 3
5 1 2 3 4
1 2 3 4 5 -> 3 moves

4 5 3 2 1
5 3 2 1 4
3 2 1 4 5
2 1 3 4 5
1 2 3 4 5 -> 4 moves

1 4 3 2 5
4 3 1 2 5
3 1 2 4 5
1 2 3 4 5 -> 3 moves

2 1 4 5 3
1 4 5 2 3 # Interesting!
4 5 1 2 3
5 1 2 3 4
1 2 3 4 5 -> 4 moves 

5 4 1 3 2
4 1 3 2 5
1 3 2 4 5
3 1 2 4 5
1 2 3 4 5 -> 4 moves
"""

"""
5 4 6 7 3 1 2
4 6 7 3 1 2 5
6 7 3 1 2 4 5
7 3 1 2 4 5 6
3 1 2 4 5 6 7
1 2 3 4 5 6 7 -> 5 moves

6 5 3 7 2 1 4
5 3 7 2 1 4 6
3 7 2 1 4 5 6
7 2 1 3 4 5 6
2 1 3 4 5 6 7
1 2 3 4 5 6 7 -> 5 moves

1 6 5 7 3 4 2
6 5 7 3 4 1 2
5 7 3 4 1 2 6
7 3 4 1 2 5 6
3 4 1 2 5 6 7
4 1 2 3 5 6 7
1 2 3 4 5 6 7 -> 6 moves

4 2 3 6 1 7 5

"""
