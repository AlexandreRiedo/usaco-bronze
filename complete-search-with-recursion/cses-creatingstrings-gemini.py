def solve(string: str):
    answers = set()
    length = len(string)
    visited = [False] * length
    current_permutation = []

    def backtrack(depth: int):
        if depth == length:
            answers.add("".join(current_permutation))
            return

        for idx in range(length):
            if not visited[idx]:
                # Mark as visited and append character
                visited[idx] = True
                current_permutation.append(string[idx])
                
                backtrack(depth + 1)
                
                # Backtrack: unmark and remove character
                visited[idx] = False
                current_permutation.pop()

    backtrack(0)
    return sorted(answers)

text = input()
answers = solve(text)

print(len(answers))
for answer in answers:
    print(answer)