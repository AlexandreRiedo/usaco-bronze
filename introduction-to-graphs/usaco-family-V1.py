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


def rec_wrap():
    def explore(curr, state, visited, target):
        if curr in visited:
            return
        if curr == target:
            nonlocal relation
            relation = state
            return

        for parent in up[curr]:
            visited.add(curr)
            explore(parent, mutate_state(state, "up"), visited, target)
            visited.remove(curr)
        for child in down[curr]:
            visited.add(curr)
            explore(child, mutate_state(state, "down"), visited, target)
            visited.remove(curr)

    visited = set()
    start = a
    target = b
    state = "NOT RELATED"
    relation = "NOT RELATED"
    explore(start, state, visited, target)

    if "ILLEGAL" in relation:
        visited = set()
        start = b
        target = a
        state = "NOT RELATED"
        relation = "NOT RELATED"
        explore(start, state, visited, target)

    return target, relation, start


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
    answer = rec_wrap()
    f.write(f"{format_answer(answer)}\n")
