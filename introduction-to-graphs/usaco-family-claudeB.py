from collections import defaultdict

with open("family.in") as f:
    num_cows, a, b = f.readline().split()
    num_cows = int(num_cows)

    down = defaultdict(set)
    up = defaultdict(set)

    for _ in range(num_cows):
        x, y = f.readline().split()
        down[x].add(y)
        up[y].add(x)


def mutate_state(state, direction):
    match direction, state:
        case "up", "NOT RELATED":
            return "MOTHER"
        case "up", "MOTHER":
            return "GRAND-MOTHER"
        case "up", "GRAND-MOTHER":
            return "GREAT-GRAND-MOTHER"
        case "up", s if "GREAT-GRAND-MOTHER" in s:
            return "GREAT-" + s
        case "up", _:
            return "ILLEGAL GOING UP"
        case "down", "MOTHER":
            return "SISTER"
        case "down", "GRAND-MOTHER":
            return "AUNT"
        case "down", s if "GREAT-GRAND-MOTHER" in s:
            return s.replace("GRAND-MOTHER", "") + "AUNT"
        case "down", s if "AUNT" in s or s == "COUSIN":
            return "COUSIN"
        case "down", _:
            return "ILLEGAL GOING DOWN"


def explore(curr, state, visited, target):
    if curr == target:
        return state
    visited.add(curr)
    for neighbors, direction in ((up[curr], "up"), (down[curr], "down")):
        for nxt in neighbors:
            if nxt in visited:
                continue
            found = explore(nxt, mutate_state(state, direction), visited, target)
            if found is not None:
                return found
    return None


def relate(start, target):
    relation = explore(start, "NOT RELATED", set(), target)
    if relation is not None and "ILLEGAL" in relation:
        # wrong direction (descendant / niece): re-run the other way
        relation = explore(target, "NOT RELATED", set(), start)
        start, target = target, start
    return target, relation or "NOT RELATED", start


def format_answer(answer):
    target, relation, start = answer
    match relation:
        case "SISTER":
            return "SIBLINGS"
        case "COUSIN":
            return "COUSINS"
        case s if "MOTHER" in s or "AUNT" in s:
            return f"{target} is the {relation.lower()} of {start}"
        case _:
            return "NOT RELATED"


with open("family.out", "w") as f:
    f.write(f"{format_answer(relate(a, b))}\n")