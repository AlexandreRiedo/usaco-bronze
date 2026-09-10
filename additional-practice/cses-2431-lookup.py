# CLAUDE's rework of my code to be clearer
from bisect import bisect_right
from itertools import accumulate

MAX_LEN = 19  # the string is past 10**18 characters well before 19-digit numbers end


def block_len(length: int) -> int:
    """Characters contributed by all numbers with exactly `length` digits."""
    return length * 9 * 10 ** (length - 1)


# chars_upto[L] = characters before the first (L+1)-digit number
chars_upto = [0, *accumulate(block_len(L) for L in range(1, MAX_LEN + 1))]
assert chars_upto[-1] >= 10**18

for _ in range(int(input())):
    pos = int(input()) - 1  # 0-indexed from here on
    length = bisect_right(chars_upto, pos)  # smallest L with chars_upto[L] > pos
    offset = pos - chars_upto[length - 1]  # 0-indexed offset inside the L-digit block
    number_idx, digit_idx = divmod(offset, length)
    number = 10 ** (length - 1) + number_idx
    print(str(number)[digit_idx])
