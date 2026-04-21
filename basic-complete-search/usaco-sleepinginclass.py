num_tests = int(input())

for _ in range(num_tests):
    num_periods = int(input())
    periods = [int(item) for item in input().split()]

    modifications = 0

    print(modifications)

"""
EXAMPLE
6
4 5 1 3 6 2

SUM CANDIDATES
- 6
- 21

9 1 3 6 2
4 6 3 6 2
4 5 4 6 2
4 5 1 9 2
4 5 1 3 8
"""

"""
EXPLORATION
6
1 2 3 1 1 1

Left To Right
3 3 1 1 1
3 3 2 1
3 3 3
"""

"""
EXPLORATION 2
5 1 4 2
6 4 2
6 6

5 4 1 2
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