import itertools
from collections import defaultdict
from math import inf

from rich import print as rprint

_ = input()
sequence = list(map(int, input().split()))


def verify(seq: list[int]) -> bool:
    num_to_positions = defaultdict(list)
    for idx, num in enumerate(seq):
        num_to_positions[num].append(idx)

    for num, positions in num_to_positions.items():
        if len(positions) <= 1:
            continue

        for pair1, pair2 in itertools.pairwise(positions):
            if any(slice_num != num for slice_num in seq[pair1 : pair2 + 1]):
                return False

    return True


def recursion(sequence: list[int]):
    seq = sequence[:]
    best = inf
    edits = 0

    def backtrack():
        nonlocal best
        nonlocal edits

        if verify(seq):
            best = min(best, edits)
            rprint(f"{seq=} {edits=}")
            return

        num_to_positions = defaultdict(list)
        for idx, num in enumerate(seq):
            num_to_positions[num].append(idx)

        for num_to_edit, positions_to_edit in num_to_positions.items():
            for num_to_swap in [
                key for key in num_to_positions.keys() if key != num_to_edit
            ]:
                edits += len(num_to_positions[num_to_edit])
                for pos in positions_to_edit:
                    seq[pos] = num_to_swap
                backtrack()
                for pos in positions_to_edit:
                    seq[pos] = num_to_edit
                edits -= len(num_to_positions[num_to_edit])

    backtrack()

    return best


print(recursion(sequence))


"""
7 0
1 2 1 2 3 50 1
"""

"""
[4, 6, 3, 8, 8, 10, 9, 6, 7, 3, 4, 6, 9, 7, 1, 4, 6, 6, 6, 5]
20 0
4 6 3 8 8 10 9 6 7 3 4 6 9 7 1 4 6 6 6 5
"""

"""
15 0
9 6 4 10 5 3 3 6 2 8 3 10 8 5 4

15 0
1 3 5 1 1 7 1 5 1 7 5 7 5 7 5

15 0
6 7 2 4 1 7 1 3 5 7 6 4 5 4 4

15 0
4 5 6 3 6 4 6 6 2 6 5 7 1 6 5
"""

"""
10 0
2 4 1 5 2 1 4 1 4 3
best with 6: 4 4 4 4 4 4 4 4 4 3 OR 1 1 1 1 1 1 1 1 1 3

10 0
1 5 3 4 5 2 4 5 1 5
best with 6: 5 5 5 5 5 5 5 5 5 5

10 0
1 1 1 2 1 4 5 3 1 3
best with 5: 1 1 1 1 1 1 1 1 1 1

10 0
4 1 1 3 5 1 3 5 5 1
best with 5: 4 1 1 1 1 1 1 1 1 1

10 0
5 3 3 2 2 5 2 4 3 3
best with 6: 3 3 3 3 3 3 3 3 3 3

10 0
1 4 1 2 3 2 1 5 1 5
best with 6: 1 1 1 1 1 1 1 1 1 1 

10 0
5 1 3 2 2 1 3 1 2 3
best with 6: 5 1 1 1 1 1 1 1 1 1 1 or 5 3 3 3 3 3 3 3 3 3 3 or 5 2 2 2 2 2 2 2 2 2
IDEA: Just blanket fill all numbers with the most popular one and count?

10 0
5 1 3 2 2 1 3 1 4 3
best with 6: 5 1 1 1 1 1 1 1 1 1 1 or 5 3 3 3 3 3 3 3 3 3 3

10 0
5 3 1 2 2 1 3 1 4 3
best with 6: 5 1 1 1 1 1 1 1 1 1 1 or 5 3 3 3 3 3 3 3 3 3 3

10 0
5 3 1 2 1 1 3 1 4 3
best with 5: 5 1 1 1 1 1 1 1 1 1 1

10 0
5 5 5 2 5 1 3 3 3 3
best with 1: 5 5 5 5 5 1 3 3 3 3

10 0
5 5 5 2 5 1 3 2 3 3
best with 6: 5 5 5 5 5 5 5 5 5 5

10 0
1 2 1 3 1 4 6 5 5 5
best with 2: 1 1 1 1 1 4 6 5 5 5

10 0
1 5 1 3 1 4 6 5 5 5
best with 6: 5 5 5 5 5 5 5 5 5 5
"""

"""
30 0
1 6 5 19 16 7 9 7 5 9 4 19 20 4 9 2 12 7 4 15 20 5 5 20 10 3 16 14 14 8

1 6 5 19 16 7 9 7 5 9 4 19 20 4 9 2 12 7 4 15 20 5 20 10 3 16 14 8
1 6 5 19 16 7 9 7 5 9 4 19 20 4 9 2 12 7 4 15 20 5 20 10 3 16 14 5
1 6 5 19 16 7 9 7 5 9 4 19 20 4 9 2 12 7 4 15 20 5 20 10 5 16 14 5
1 6 5 19 16 7 9 7 5 9 4 19 20 4 9 2 12 7 4 15 20 5 20 5 5 16 14 5
1 6 5 19 16 7 9 7 5 9 4 19 20 4 9 2 12 7 4 5 20 5 20 5 5 16 14 5
1 6 5 19 16 7 9 7 5 9 4 19 20 4 9 2 5 7 4 5 20 5 20 5 5 16 14 
1 6 5 19 16 7 9 7 5 9 4 19 20 4 9 5 5 7 4 5 20 5 20 5 5 16 14 
1 5 5 19 16 7 9 7 5 9 4 19 20 4 9 5 5 7 4 5 20 5 20 5 5 16 14 
5 5 5 19 16 7 9 7 5 9 4 19 20 4 9 5 5 7 4 5 20 5 20 5 5 16 14
5 5 5 19 16 7 9 7 5 9 4 19 20 4 9 5 5 7 4 5 20 5 20 5 5 16 5 
5 5 5 19 5 7 9 7 5 9 4 19 20 4 9 5 5 7 4 5 20 5 20 5 5 5 5
5 5 5 5 5 7 9 7 5 9 4 5 20 4 9 5 5 7 4 5 20 5 20 5 5 5 5 
5 5 5 5 5 7 9 7 5 9 4 5 5 4 9 5 5 7 4 5 5 5 5 5 5 5 5 
5 5 5 5 5 7 9 7 5 9 5 5 5 5 9 5 5 7 5 5 5 5 5 5 5 5 5 
5 5 5 5 5 7 9 7 5 9 5 5 5 5 9 5 5 7 5 5 5 5 5 5 5 5 5 
"""

"""
[1,2,2,2,1,1,1]
1 2 2 2 1 1 1
"""
