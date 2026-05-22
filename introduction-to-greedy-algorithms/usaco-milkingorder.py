with open("milkorder.in") as file:
    num_cows, num_hierarchy, num_position = map(int, file.readline().strip().split())
    hierarchy = [
        int(num) for num in reversed(file.readline().strip().split())
    ]  # highest priorty at [-1]
    ordering = []
    for _ in range(num_position):
        cow, order = map(int, file.readline().strip().split())
        ordering.append((cow, order - 1))
    ordering.sort(key=lambda x: x[1], reverse=True)  # highest priority at [-1]


def solve(hierarchy, ordering, num_cows):
    for idx in range(num_cows):
        if not ordering:
            if 1 in hierarchy and hierarchy[-1] != 1:
                hierarchy.pop()
            else:
                return idx + 1
        else:
            # Use the ordering's cow if we're on it
            if ordering[-1][1] == idx:
                if ordering[-1][0] == 1:
                    return idx + 1
                ordering.pop()
            # If the ordering's cow is in the hierarchy, we must first exhaust the cows
            # of the hierarchy before using the ordering cow.
            elif hierarchy and ordering[-1][0] in hierarchy:
                if hierarchy[-1] == 1:
                    return idx + 1
                hierarchy.pop()
            # If the ordering's cow isn't in the hierarchy
            else:
                if 1 in hierarchy and hierarchy[-1] != 1:
                    hierarchy.pop()
                else:
                    return idx + 1


with open("milkorder.out", "w") as f:
    f.write(f"{solve(hierarchy, ordering, num_cows)}\n")

"""
3 4 5 1
-> 4 is the answer
"""
