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
    if direction == "up":
        if state == "NOT RELATED":
            state = "MOTHER"
        elif state == "MOTHER":
            state = "GRAND-MOTHER"
        elif state == "GRAND-MOTHER":
            state = "GREAT-GRAND-MOTHER"
        elif "GREAT-GRAND-MOTHER" in state:
            state = "GREAT-" + state
        else:
            state = "ILLEGAL GOING UP"
    elif direction == "down":
        if state == "MOTHER":
            state = "SISTER"
        elif state == "GRAND-MOTHER":
            state = "AUNT"
        elif "GREAT-GRAND-MOTHER" in state:
            state = state.replace("GRAND-MOTHER", "") + "AUNT"
        elif "AUNT" in state:
            state = "COUSIN"
        elif state == "COUSIN":
            state = "COUSIN"
        else:
            state = "ILLEGAL GOING DOWN"
    return state


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
    output = ""

    if relation == "SISTER":
        output = "SIBLINGS"
    elif "MOTHER" in relation:
        output = f"{target} is the {relation.lower()} of {start}"
    elif "AUNT" in relation:
        output = f"{target} is the {relation.lower()} of {start}"
    elif relation == "COUSIN":
        output = "COUSINS"
    else:
        output = "NOT RELATED"

    return output


with open("family.out", "w") as f:
    f.write(f"{format_answer(relate(a, b))}\n")