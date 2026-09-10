from bisect import bisect_left as bl
from itertools import accumulate


def find_size(digits: int):
    return digits * (10**digits - 10 ** (digits - 1))


MAX_K, NUM_DIGITS = 10**18, 20
sizes = [0] + list(accumulate(find_size(x) for x in range(1, NUM_DIGITS)))
assert sizes[-1] > MAX_K

for _ in range(int(input())):
    k = int(input())
    digits = bl(sizes, k)

    idx = k - sizes[digits - 1] - 1
    num_pos, num_shift = divmod(idx, digits)

    ans = str(10 ** (digits - 1) + num_pos)[num_shift]
    print(ans)


# CLAUDE's Suggestions for variable renames
#
#   Original            What it holds                               Clearer name
#   -----------------   -----------------------------------------   -----------------
#   find_size(digits)   Characters from all numbers with exactly    block_len(length)
#                       `length` digits (computes, not searches)
#
#   sizes               Prefix sums: chars_upto[L] = characters     chars_upto
#                       from all numbers with at most L digits
#
#   digits              Digit count of the target number            length
#
#   idx                 0-indexed offset inside the L-digit block   offset
#
#   num_pos             Index of the number within its block,       number_idx
#                       counted from 10**(L - 1)
#
#   num_shift           Index of the digit within that number       digit_idx
#                       (0 = leftmost)
#
#   NUM_DIGITS          Upper bound on number length                MAX_LEN
#                       (was exclusive via range; now inclusive)
