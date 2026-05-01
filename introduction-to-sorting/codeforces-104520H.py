from collections import deque

from rich import print as rprint

num_elements = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b_sort = deque(sorted(b))

rprint(f"{b_sort=}")

"""
5
3

5 4
3 2

5 4 -1
3 2 4

4
2

4 -1
2 4

-1
4


5*3 + 5*3+4*2 + 5*3+4*2+-1*4 + 4*2 + 4*2+-1*4 + -1*4 = 65
"""

"""
-1 4 5
4  3 2
"""

"""
1 2 3 4
5 6 7 8


1
5

1 2
5 6

1 2 3
5 6 7

1 2 3 4
5 6 7 8

2
6

2 3
6 7

2 3 4
6 7 8

3
7

3 4
7 8

4 
8

1*5 + 1*5+2*6 + 1*5+2*6+3*7 + 1*5+2*6+3*7+4*8 + 2*6 + 2*6+3*7 + 2*6+3*7+4*8 + 3*7 + 3*7+4*8 + 4*8 = 346
"""
