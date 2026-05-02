import itertools
from collections import Counter, defaultdict

_ = input()
seq = list(map(int, input().split()))

num_to_groups = defaultdict(list)
idx = 0
for key, group in itertools.groupby(seq):
    num_to_groups[key].append(idx)
    idx += len(list(group))

left, right = 0, len(seq)  # right is exclusive
for left, num in enumerate(seq):
    if len(num_to_groups[num]) != 1:
        break
for _, num in enumerate(reversed(seq)):
    if len(num_to_groups[num]) != 1:
        break
    right -= 1


if left >= right:
    print(0)
else:
    max_to_edit = right - left
    num_counter = Counter(seq[left:right])
    edits = max_to_edit - num_counter.most_common()[0][1]
    print(edits)

"""
TEST CASE 12 FAIL
999 0
1 2 1 
3 4 3 
5 6 5 
7 8 7 
9 10 9 
11 12 11
13 14 13 
15 16 15 
17 18 17 etc...
"""

"""
1
1 2 3 4 1
3
"""

"""
10 0
1 2 1 3 1 4 6 5 5 5
best with 2: 1 1 1 1 1 4 6 5 5 5

10 0
1 5 1 3 1 4 6 5 5 5
best with 6: 5 5 5 5 5 5 5 5 5 5
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
"""
