from typing import NamedTuple

from rich import print as rprint


class Subgrid(NamedTuple):
    best_score: int
    x: int
    y: int


def get_scores(x, y, beauty):
    tl, tr, bl, br = (
        beauty[y][x],
        beauty[y][x + 1],
        beauty[y + 1][x],
        beauty[y + 1][x + 1],
    )

    return [tl, tr, bl, br]


def count_placed(x, y, placement):
    tl, tr, bl, br = (
        placement[y][x],
        placement[y][x + 1],
        placement[y + 1][x],
        placement[y + 1][x + 1],
    )

    return sum(1 for cell in [tl, tr, bl, br] if cell == "C")


N = int(input())
beauty = [list(map(int, input().split())) for _ in range(N)]
subgrids = []
placement = [["."] * N for _ in range(N)]

# Mapping out the subgrids
for y in range(N - 1):
    for x in range(N - 1):
        tl, tr, bl, br = get_scores(x, y, beauty)
        best_score = max(tl, tr, bl, br) + sorted([tl, tr, bl, br], reverse=True)[1]
        subgrids.append(Subgrid(best_score, x, y))

        rprint(f"{x=} {y=}")
        rprint(f"{beauty[y][x]} {beauty[y][x + 1]}")
        rprint(f"{beauty[y + 1][x]} {beauty[y + 1][x + 1]}")
        rprint(f"{best_score=}")
        rprint(f"{subgrids[-1]}")
        rprint("")

subgrids.sort(key=lambda x: x.best_score, reverse=True)
rprint(f"{subgrids=}")

# Initial Placement
for subgrid in subgrids:
    x, y = subgrid.x, subgrid.y
    scores = get_scores(x, y, beauty)
    sorted_scores = sorted(scores)

    rprint("")
    rprint(f"{x=} {y=}")
    for row in placement:
        rprint(f"{row}")
    rprint(f"\n{subgrids=}")

    while count_placed(x, y, placement) < 2:
        # An unresolvable tie: we skip and we'll come back later on
        if len(sorted_scores) >= 3 and (
            sorted_scores[-1] == sorted_scores[-2] == sorted_scores[-3]
        ):
            break

        # Placing "C"
        curr_best = sorted_scores.pop()
        for idx, score in enumerate(scores):
            if score == curr_best:
                if idx == 0 and placement[y][x] != "X":
                    placement[y][x] = "C"
                    break
                elif idx == 1 and placement[y][x + 1] != "X":
                    placement[y][x + 1] = "C"
                    break
                elif idx == 2 and placement[y + 1][x] != "X":
                    placement[y + 1][x] = "C"
                    break
                elif idx == 3 and placement[y + 1][x + 1] != "X":
                    placement[y + 1][x + 1] = "C"
                    break
    else:
        # Placing "X" when it finishes normally
        for idx, score in enumerate(scores):
            if idx == 0 and placement[y][x] == ".":
                placement[y][x] = "X"
            elif idx == 1 and placement[y][x + 1] == ".":
                placement[y][x + 1] = "X"
            elif idx == 2 and placement[y + 1][x] == ".":
                placement[y + 1][x] = "X"
            elif idx == 3 and placement[y + 1][x + 1] == ".":
                placement[y + 1][x + 1] = "X"


"""
3
4 4 4
2 1 6
3 3 9

...
cxc
cxc
"""

"""
3
4 1 8
2 3 4
5 5 9
"""
