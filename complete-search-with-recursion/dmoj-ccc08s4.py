NUM_CARDS = 4
MAX = 24

num_card_hands = int(input())
for _ in range(num_card_hands):
    cards = [int(input()) for _ in range(NUM_CARDS)]

    result = 0
    used = [False for _ in range(NUM_CARDS)]

    def solve(num_used: int = 0, value: int = 0):
        global result

        if num_used == NUM_CARDS:
            if value <= MAX:
                result = max(result, value)

        for idx, card in enumerate(cards):
            if used[idx]:
                continue

            if all(not bool for bool in used):
                used[idx] = True
                solve(num_used + 1, card)
                used[idx] = False
            else:
                used[idx] = True
                solve(num_used + 1, value + card)
                solve(num_used + 1, value - card)
                solve(num_used + 1, value * card)
                if value % card == 0:
                    solve(num_used + 1, value / card)  # type: ignore

                used[idx] = False

    solve()
    print(result)
