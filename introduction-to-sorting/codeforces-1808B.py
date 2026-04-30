import itertools
import sys


def solve():
    num_cards, _ = map(int, sys.stdin.readline().rstrip().split())
    card_numbers = [
        list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(num_cards)
    ]

    if num_cards <= 1:
        return 0

    winnings = 0
    for card_a, card_b in itertools.combinations(card_numbers, 2):
        winnings += sum(abs(num_a - num_b) for num_a, num_b in zip(card_a, card_b))

    return winnings


num_tests = int(sys.stdin.readline().rstrip())
for _ in range(num_tests):
    sys.stdout.write(f"{solve()}\n")
