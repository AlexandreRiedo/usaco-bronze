text = [char for char in input()]


def solve(depth: int, string: list, indices=None, answers=None):
    if indices is None:
        indices = []
    if answers is None:
        answers = set()

    if depth == len(string):
        answers.add("".join(string[index] for index in indices))

    for index in [idx for idx in range(len(string)) if idx not in indices]:
        indices.append(index)
        solve(depth + 1, string, indices, answers)
        indices.pop()

    return sorted(answers)


answers = solve(0, text)
print(len(answers))
[print(answer) for answer in answers]
