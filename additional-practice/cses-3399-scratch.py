from itertools import permutations

from rich import print as rprint

# for _ in range(int(input())):
#     n, a, b = map(int, input().split())

N = 4
log = set()
scores = set()
for a_cards in permutations(range(1, N + 1)):
    for b_cards in permutations(range(1, N + 1)):
        a_score, b_score = (
            sum(a > b for a, b in zip(a_cards, b_cards)),
            sum(b > a for a, b in zip(a_cards, b_cards)),
        )
        # log.add((f"a={a_score}", f"b={b_score}"))
        scores.add((a_score, b_score))
        rprint(f"{a_score=} {b_score=}")
        rprint(f"[blue]{a_cards}")
        rprint(f"[purple]{b_cards}")
        rprint()

# rprint(f"{sorted(log)=}")
rprint(f"{scores=}")

# test = {(a, b) for a in range(1, N) for b in range(1, N) if a + b <= N}
# test.add((0, 0))
# assert scores == test
