from rich import print as rprint

num_cows = int(input())
order = list(input())


def find_right_wrong_G(order, right=len(order) - 1):
    """
    -1 means the ordering is already perfect!
    """
    for i in range(right, -1, -1):
        if order[i] == "G" and i % 2 == 0:
            return i
    else:
        return -1


def flip_scores(order):
    """
    Note that idx are thought of as 1-indexed in the counts
    returns: list[tuple(score, idx)]
    """
    count = []
    even_G = 0
    odd_G = 0

    for idx, cow in enumerate(order):
        if cow == "G" and idx % 2 == 0:
            odd_G += 1
        elif cow == "G" and idx % 2 == 1:
            even_G += 1

        if idx % 2 == 0:
            count.append((0))  # on an "odd", the count doesn't change
        elif idx % 2 == 1:
            count.append((odd_G - even_G))

    return count


rprint(f"{find_right_wrong_G(order)=}")
rprint(f"{flip_scores(order)=}")

"""
GGGHGHHGHHHGHG
.X.....X...X.X
G score: 4

HGHGGGHGHHHGHG
.X.X.X.X...X.X
G score: 6

[0,0,0,1,0,0,2]
"""

"""
GHGGHGHGHG -> 4
HGGGHGHGHG -> 5
(This needs to flip by exploring potential anchors on the left)
"""

"""
GGGHGHHHGHHGHG
.X.........X.X
G score: 3
"""

"""
FLIPPING EVEN
GGGHGH
.X....
HGHGGG
.X.X.X
2->5 (even goes to odd, odd goes to even, aka flip the score)

FLIPPING ODD AMOUNT
GGGHG
.X...
GHGGG
...X.
1->5, 2->4, 3->3, 5->1 (even goes to even, odd goes to odd)
"""

"""
"".join(random.choice("GH") for _ in range(12))
"""

"""
HGHGGHGHHHHG
.X.X.......X
-> 0

HGGGGGHHHGHH
.X.X.X...X..
-> 0

VIP VIP VIP CASE CASE CASE
GGHHHHHGHHHH -> flip @4
.X.....X....
HHGGHHHGHHHH -> flip @3
...X...X....
GHHGHHHGHHHH -> flip @2
...X...X....
HGHGHHHGHHHH = 3 flips to achieve perfection
.X.X...X....

HHGGGGGGGGGG -> flip @3
...X.X.X.X.X
GHHGGGGGGGGG -> flip @2
...X.X.X.X.X
HGHGGGGGGGGG = 2 flipts for perfection
.X.X.X.X.X.X

GGHHGGGGGGHH -> flip @4
.X...X.X.X..
HHGGGGGGGGHH -> flip @3
...X.X.X.X..
GHHGGGGGGGHH -> flip @2
...X.X.X.X..
HGHGGGGGGGHH = 3 flips to achieve perfection
.X.X.X.X.X..

VIP VIP VIP CASE CASE CASE
GHHHHHGGHGGH flip @12
.......X.X..
HGGHGGHHHHHG flip @5 (A), flip @8 (B)
.X...X.....X
FORK A BELOW --------
GHGGHGHHHHHG flip @2
...X.X.....X
HGGGHGHHHHHG = 3 flips to achieve perfection
.X.X.X.....X
FORK B below --------
HHGGHGGHHHHG flip @3
...X.X.....X
GHHGHGGHHHHG flip @2
...X.X.....X
HGHGHGGHHHHG = 4 flips to achieve perfection
.X.X.X.....X
"""

"""

"""