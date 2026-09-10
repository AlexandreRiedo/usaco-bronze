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
