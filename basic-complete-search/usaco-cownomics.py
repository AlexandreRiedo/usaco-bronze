import itertools
import sys

sys.stdin = open("cownomics.in", "r")
sys.stdout = open("cownomics.out", "w")

num_lines, num_chars = map(int, sys.stdin.readline().strip().split())
spotties = [sys.stdin.readline().strip() for _ in range(num_lines)]
plains = [sys.stdin.readline().strip() for _ in range(num_lines)]


count = 0
for pos_a, pos_b, pos_c in itertools.combinations(range(num_chars), 3):
    spotty_set = set()
    for spotty in spotties:
        spotty_set.add((spotty[pos_a], spotty[pos_b], spotty[pos_c]))

    plain_set = set()
    for plain in plains:
        plain_set.add((plain[pos_a], plain[pos_b], plain[pos_c]))

    if not plain_set & spotty_set:
        count += 1

sys.stdout.write(f"{count}\n")
