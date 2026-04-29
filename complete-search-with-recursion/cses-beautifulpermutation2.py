n = int(input())
n_set = set(range(1, n + 1))


def solve(
    n: int,
    used: set[int] = set(),
    current_permutation: list[int] = [],
    results=[],
    is_solved=[False],
):
    # if is_solved[0]:
    #     return
    # else:
    if len(current_permutation) == n:
        is_solved[0] = True
        # print(" ".join([str(item) for item in current_permutation]))
        # return
        results.append(tuple(current_permutation))

    for num in range(1, n + 1):
        if num in used:
            continue
        if len(current_permutation) == 0:
            used.add(num)
            current_permutation.append(num)
            solve(n, used, current_permutation, results, is_solved)
            current_permutation.pop()
            used.remove(num)
        elif abs(num - current_permutation[-1]) != 1:
            used.add(num)
            current_permutation.append(num)
            solve(n, used, current_permutation, results, is_solved)
            current_permutation.pop()
            used.remove(num)

    return results


print(solve(n)[0])
print(sorted(solve(n))[0])
