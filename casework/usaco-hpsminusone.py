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
    drawing_symbols = draws[elsie_left] | draws[elsie_right]
    losing_symbols = wins[elsie_left] | wins[elsie_right]
    left_killer_symbols = loses[elsie_left] - wins[elsie_right]
    right_killer_symbols = loses[elsie_right] - wins[elsie_left]
    # rprint(f"{drawing_symbols=}")
    # rprint(f"{losing_symbols=}")
    # rprint(f"{killer_symbols=}")
    # rprint(f"{left_killer_symbols=}")
    # rprint(f"{right_killer_symbols=}")

    # Case (left_killer, right_killer + draw breaker)
    left_case = {
        (left, right)
        for left in left_killer_symbols
        for right in (right_killer_symbols - draws[elsie_left])
    }

    # Case (left_killer + draw breaker, right_killer)
    right_case = {
        (left, right)
        for left in (left_killer_symbols - draws[elsie_right])
        for right in right_killer_symbols
    }

    # Case (killer, loses)
    case_1 = {(killer, lose) for killer in killer_symbols for lose in losing_symbols}

    # Case (killer, draws)
    case_2 = {(killer, draw) for killer in killer_symbols for draw in drawing_symbols}

    # Case (loses, killer)
    case_3 = {(lose, killer) for killer in killer_symbols for lose in losing_symbols}

    # Case (draws, killer)
    case_4 = {(draw, killer) for killer in killer_symbols for draw in drawing_symbols}

    print(len(left_case | right_case | case_1 | case_2 | case_3 | case_4))
