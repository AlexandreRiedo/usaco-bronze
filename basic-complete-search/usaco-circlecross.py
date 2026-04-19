import itertools
import string
import sys

sys.stdin = open("circlecross.in", "r")
sys.stdout = open("circlecross.out", "w")

crossings = input()

crossing_pairs = 0

for a, b in itertools.combinations(string.ascii_uppercase, 2):
    a_start = crossings.find(a)
    a_end = crossings.find(a, a_start + 1)

    b_start = crossings.find(b)
    b_end = crossings.find(b, b_start + 1)

    if a_start < b_start < a_end < b_end:
        crossing_pairs += 1
    elif b_start < a_start < b_end < a_end:
        crossing_pairs += 1

print(crossing_pairs)
