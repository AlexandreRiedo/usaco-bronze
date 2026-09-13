from math import inf

SUB = 10


def verify(A, B, cA, cB, fA, nA, nB):
    return cA * ((B + nB) // cB) + (A + nA) >= fA


def solve(A, B, cA, cB, fA):
    init = ((B // cB) * cA) + A
    if init >= fA:
        return 0

    ans = inf
    for x in range(SUB + 1):
        if all(
            verify(A, B, cA, cB, fA, nA, nB)
            for nA, nB in zip(range(x + 1), range(x, -1, -1))
        ):
            ans = min(ans, x)
    return ans


for _ in range(int(input())):
    A, B, cA, cB, fA = map(int, input().split())
    print(solve(A, B, cA, cB, fA))
