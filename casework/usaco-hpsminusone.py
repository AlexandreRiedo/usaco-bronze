from collections import defaultdict

num_symbols, num_games = map(int, input().split())
draws = defaultdict(set)
wins = defaultdict(set)
loses = defaultdict(set)

for i in range(1, num_symbols + 1):
    rules = input()
    for j, char in enumerate(rules, start=1):
        if char == "D":
            draws[i].add(j)
            draws[j].add(i)
        elif char == "W":
            wins[i].add(j)
            loses[j].add(i)
        elif char == "L":
            loses[i].add(j)
            wins[j].add(i)

# rprint(f"{draws=}")
# rprint(f"{wins=}")
# rprint(f"{loses=}")

for _ in range(num_games):
    elsie_left, elsie_right = map(int, input().split())
    count = 0

    killer_symbols = loses[elsie_left] & loses[elsie_right]
    # rprint(f"{killer_symbols=}")
    if len(killer_symbols) == 0:
        print(count)
    else:
        drawing_symbols = draws[elsie_left] | draws[elsie_right]
        losing_symbols = wins[elsie_left] | wins[elsie_right]
        # rprint(f"{drawing_symbols=}")
        # rprint(f"{losing_symbols=}")

        # Case (killer, killer)
        count += len(killer_symbols) * len(killer_symbols)

        # Case (killer, loses)
        count += len(killer_symbols) * len(losing_symbols)

        # Case (killer, draws)
        count += len(killer_symbols) * len(drawing_symbols)

        # Case (loses, killer)
        count += len(losing_symbols) * len(killer_symbols)

        # Case (draws, killer)
        count += len(drawing_symbols) * len(killer_symbols)

        print(count)

"""
SAMPLE INPUT
2 2 (Wboth Wboth)
2 3 (Wboth Loses)
2 1 (Wboth Draws)
1 2 (Draws Wboth)
3 2 (Loses Wboth)
"""
