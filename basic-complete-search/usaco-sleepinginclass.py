import itertools
from math import inf

num_tests = int(input())


def get_target_sums(periods):
    max_periods = max(periods)
    target_sums = set(
        filter(lambda x: x >= max_periods, set(itertools.accumulate(periods)))
    )
    return target_sums


def calculate_modifications(periods, target_sum: int):
    modifications = 0
    equalized_periods = [periods[0]]

    for period in periods[1:]:
        if equalized_periods[-1] > target_sum:
            return inf
        elif equalized_periods[-1] < target_sum:
            equalized_periods[-1] += period
            modifications += 1
        elif equalized_periods[-1] == target_sum:
            equalized_periods.append(period)

    if len(set(equalized_periods)) != 1:
        return inf

    return modifications


for _ in range(num_tests):
    num_periods = int(input())
    periods = [int(item) for item in input().split()]
    target_sums = get_target_sums(periods)

    min_modifications = inf
    for target_sum in target_sums:
        min_modifications = min(
            min_modifications, calculate_modifications(periods, target_sum)
        )

    print(min_modifications)


"""
1_000_000
"""

"""
EXAMPLE
6
4 5 1 3 6 2

SUM CANDIDATES
- 6
- 21

9 1 3 6 2 (DEAD)
4 6 3 6 2 (DEAD)
4 5 4 6 2 (DEAD)
4 5 1 9 2 (DEAD)
4 5 1 3 8 (DEAD)

EXPLORATION
4 5 1 1 1 8
4 5 1 2 8
9 1 2 8
9 1 10
10 10


IDEA : VALID TARGET SUMS
8 (max)
4+5=9
4+5+1=10
4+5+1+1=11
4+5+1+1+1=12
4+5+1+1+1+8 = 20
"""

"""
EXPLORATION
6
1 2 3 1 1 1

Left To Right
3 3 1 1 1
3 3 2 1
3 3 3

IDEA : VALID TARGET SUMS
3 (max)
1+2=3
1+2+3=6
1+2+3+1=7
1+2+3+1+1=8
1+2+3+1+1+1=9
"""

"""
EXPLORATION 2
5 1 4 2
6 4 2
6 6

5 4 1 2
9 1 2
9 3
12

2 5 1 4
2 6 4
2 10
12
"""

"""
SUM CANDIDATES IDEA
- The min candidate is the starting max value of the list
- The max candidate is the sum of all numbers of the list
"""
