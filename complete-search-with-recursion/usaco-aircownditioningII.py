from math import inf
from typing import NamedTuple

NUM_STALLS = 100


class Cow(NamedTuple):
    start: int
    end: int
    cooling_needs: int


class Conditioner(NamedTuple):
    start: int
    end: int
    cooling: int
    price: int


num_cows, num_conditioners = map(int, input().split())
cows = [Cow(*map(int, input().split())) for _ in range(num_cows)]
cows.sort(key=lambda x: (x.start, x.end))
conditioners = [Conditioner(0, 0, 0, 0)] + [
    Conditioner(*map(int, input().split())) for _ in range(num_conditioners)
]
conditioners.sort(key=lambda x: (x.start, x.end))

cooling_needed = [0 for _ in range(NUM_STALLS + 1)]
for cow in cows:
    for i in range(cow.start, cow.end + 1):
        cooling_needed[i] += cow.cooling_needs

cooling = [0 for _ in range(NUM_STALLS + 1)]
min_money = inf


def solve(idx: int = 1, money_used: int = 0):
    global min_money

    if idx == num_conditioners + 1:
        for i in range(conditioners[idx - 1].start, NUM_STALLS + 1):
            if cooling[i] < cooling_needed[i]:
                return

        min_money = min(min_money, money_used)
        return

    prev_start = conditioners[idx - 1].start
    for i in range(prev_start, conditioners[idx].start):
        if cooling[i] < cooling_needed[i]:
            return

    for i in range(conditioners[idx].start, conditioners[idx].end + 1):
        cooling[i] += conditioners[idx].cooling
    solve(idx + 1, money_used + conditioners[idx].price)
    for i in range(conditioners[idx].start, conditioners[idx].end + 1):
        cooling[i] -= conditioners[idx].cooling
    solve(idx + 1, money_used)


solve()
print(min_money)
