from rich import print as rprint  # noqa: F401 # pyright: ignore[reportUnusedImport]


def get_subgrid(x, y, grid):
    return [grid[y][x], grid[y][x + 1], grid[y + 1][x], grid[y + 1][x + 1]]


def count_placed(x, y, placement):
    return sum(1 for cell in get_subgrid(x, y, placement) if cell == "C")


N = int(input())
beauty = [list(map(int, input().split())) for _ in range(N)]
subgrids = []
placement = [["."] * N for _ in range(N)]
placed = 0

# Mapping out the subgrids
for y in range(N - 1):
    for x in range(N - 1):
        tl, tr, bl, br = get_subgrid(x, y, beauty)
        best_score = max(tl, tr, bl, br) + sorted([tl, tr, bl, br], reverse=True)[1]
        subgrids.append((best_score, x, y))

while placed != len(subgrids):
    for _, x, y in subgrids:
        curr = []
        open_slots = 0

        for loc_y in [y, y + 1]:
            for loc_x in [x, x + 1]:
                curr.append(
                    [(beauty[loc_y][loc_x], placement[loc_y][loc_x], loc_x, loc_y)]
                )
                if placement[loc_y][loc_x] == ".":
                    open_slots += 1

        curr.sort(key=lambda x: x[0], reverse=True)
        # for idx, (curr_score, curr_placement, curr_y, curr_x) in curr:
        #     if curr_placement != "." or open_slots > 0:
        #         continue
        #     else:
        #         tie_breaker = sum(
        #             1 for slot in curr[idx:] if slot[1] == "." and slot[0] == curr_score
        #         )
        #         if idx == 0 and tie_breaker:
        #             placement[y][x] = "C"
        #             open_slots -= 1
        #         elif idx == 1 and tie_breaker:
        #             placement[y][x] = "C"
        #             open_slots -= 1
        #         elif idx == 2 and tie_breaker:
