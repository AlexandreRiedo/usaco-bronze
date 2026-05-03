import itertools
import sys
from math import inf
from operator import itemgetter
from typing import NamedTuple

NEW_COWS = 2


class Gap(NamedTuple):
    length: int
    start: int
    end: int


def get_gaps(stalls: list) -> list:
    gaps = []
    idx = 0
    for key, group in itertools.groupby(stalls):
        group = list(group)
        length = len(group)
        if key == 0:
            gaps.append(Gap(length, idx, idx + length))
        idx += length
    gaps.sort(reverse=True, key=itemgetter(0))

    return gaps


def fill_gap(stalls: list, gaps: list, pick_gap: int = 0) -> list:
    edit = stalls[:]
    gap_len, gap_start, gap_end = gaps[pick_gap]

    if gap_start == 0:
        edit[gap_start] = 1
    elif gap_end == len(stalls):
        edit[gap_end - 1] = 1
    else:
        if gap_len % 2 == 1:
            edit[gap_start + ((gap_len - 1) // 2)] = 1
        else:
            edit[gap_start + (gap_len // 2)] = 1

    return edit


sys.stdin = open("socdist1.in")
sys.stdout = open("socdist1.out", "w")

num_stalls = int(input())
stalls = [int(char) for char in input()]


def solve(stalls):
    for _ in range(NEW_COWS):
        gaps = get_gaps(stalls)
        stalls = fill_gap(stalls, gaps)

    D = inf
    one_pos = []
    for idx, num in enumerate(stalls):
        if num == 1:
            one_pos.append(idx)
    for idx_a, idx_b in zip(range(len(one_pos) - 1), range(1, len(one_pos))):
        D = min(D, one_pos[idx_b] - one_pos[idx_a])

    return D


print(solve(stalls))

"""
14
10001001000010

IDEA: Find biggest gaps, then plug the cows in the middle
"""

"""
0110110000
0110011111

000100001

00000000000111000
00000100000111000
10000100000111000
3 is the answer?

"""
