from rich import print as rprint

num_cows = int(input())
order = list(input())


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
            pass
        elif idx % 2 == 1:
            count.append((odd_G - even_G, idx))

    return sorted(count, key=lambda x: (x[0], x[1]), reverse=True)


count_flips = 0
scores = flip_scores(order)
rprint(f"{order=}")
rprint(f"{scores=}")
while scores[0][0] > 0:
    count_flips += 1
    order[0 : scores[0][1] + 1] = reversed(order[0 : scores[0][1] + 1])
    scores = flip_scores(order)
    rprint(f"In Loop: {order=}")
    rprint(f"In Loop: {scores=}")

print(count_flips)

"""
INITIAL EXAMPLE
GGGHGHHGHHHGHG
.X.....X...X.X
G score: 4

HGHGGGHGHHHGHG
.X.X.X.X...X.X
G score: 6
"""

"""
RANDOM EXPLORATION
HHGHGHGHGHHG -> flip @10
...........X
HGHGHGHGHHHG
.X.X.X.X...X

HHHGGGHGHGGH
...X.X.X.X..

GHGGGGGGGGHH
...X.X.X.X..
HGGGGGGGGGHH
.X.X.X.X.X..

GHGGHGHHHGGH
...X.X...X..
HGGGHGHHHGGH
.X.X.X....X.

GGGGHHGHHHHG
.X.X.......X
HHHGHHGGGGHG
...X...X.X.X

GGGGGGGHGGGG
.X.X.X...X.X
GGGGHGGGGGGG
.X.X.X.X.X.X
"""


"""
RANDOM EXPLORATION V2

HHGGHGGH
...X.X..

GHGGHGHH
...X.X..
GGHGHGHH
.X.X.X..
"""
