import sys
from itertools import groupby
from operator import itemgetter

sys.stdin = open("notlast.in")
sys.stdout = open("notlast.out", "w")

NAMES = ["Bessie", "Elsie", "Daisy", "Gertie", "Annabelle", "Maggie", "Henrietta"]
totals = dict.fromkeys(NAMES, 0)

n = int(input())
for _ in range(n):
    name, amount = input().split()
    totals[name] += int(amount)

# Sort by production, then group into tiers of equal production.
by_production = itemgetter(1)
sorted_cows = sorted(totals.items(), key=by_production)
tiers = [
    [name for name, _ in group] for _, group in groupby(sorted_cows, key=by_production)
]

# We need a second-lowest tier with exactly one cow in it.
if len(tiers) < 2 or len(tiers[1]) > 1:
    print("Tie")
else:
    print(tiers[1][0])
