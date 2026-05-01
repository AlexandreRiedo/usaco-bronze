import sys
from collections import defaultdict

sys.stdin = open("notlast.in", "r")
sys.stdout = open("notlast.out", "w")

NAMES = ["Bessie", "Elsie", "Daisy", "Gertie", "Annabelle", "Maggie", "Henrietta"]
cows = {name: 0 for name in NAMES}

num_entries = int(input())
for _ in range(num_entries):
    name, production = input().split()
    cows[name] += int(production)

production_to_cows = defaultdict(list)
for cow_name, production in sorted(cows.items(), key=lambda x: x[1]):
    production_to_cows[production].append(cow_name)

if len(production_to_cows) == 1:
    print("Tie")
else:
    desired_value = list(production_to_cows.keys())[1]

    if len(production_to_cows[desired_value]) > 1:
        print("Tie")
    else:
        print(production_to_cows[desired_value][0])
