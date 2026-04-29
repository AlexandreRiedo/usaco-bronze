import sys

sys.setrecursionlimit(1_000_000)

n = int(input())
n_set = set(range(1, n + 1))


def solve(
    n: int,
    used: set[int] = set(),
    current_permutation: list[int] = [],
    results=[],
    is_solved=[False],
):
    if is_solved[0]:
        return
    else:
        if len(current_permutation) == n:
            is_solved[0] = True
            print(" ".join([str(item) for item in current_permutation]))
            return
        for num in range(1, n + 1):
            if is_solved[0]:
                return

            if num in used:
                continue
            if len(current_permutation) == 0:
                used.add(num)
                current_permutation.append(num)
                solve(n, used, current_permutation, results, is_solved)
                current_permutation.pop()
                used.remove(num)
            elif abs(num - current_permutation[-1]) != 1:
                used.add(num)
                current_permutation.append(num)
                solve(n, used, current_permutation, results, is_solved)
                current_permutation.pop()
                used.remove(num)

for i in range(1, 21):
    is_solved = [False]
    (solve(i, is_solved=is_solved))
    if not is_solved[0]:
        print("NO SOLUTION")

"""
1
NO SOLUTION
NO SOLUTION
2 4 1 3
1 3 5 2 4
1 3 5 2 4 6
1 3 5 2 6 4 7
1 3 5 2 6 8 4 7
1 3 5 2 4 7 9 6 8
1 3 5 2 4 6 8 10 7 9
1 3 5 2 4 6 8 10 7 9 11
1 3 5 2 4 6 8 10 7 11 9 12
1 3 5 2 4 6 8 10 7 11 13 9 12
1 3 5 2 4 6 8 10 7 9 12 14 11 13
1 3 5 2 4 6 8 10 7 9 11 13 15 12 14
1 3 5 2 4 6 8 10 7 9 11 13 15 12 14 16
1 3 5 2 4 6 8 10 7 9 11 13 15 12 16 14 17
1 3 5 2 4 6 8 10 7 9 11 13 15 12 16 18 14 17
1 3 5 2 4 6 8 10 7 9 11 13 15 12 14 17 19 16 18
1 3 5 2 4 6 8 10 7 9 11 13 15 12 14 16 18 20 17 19
"""