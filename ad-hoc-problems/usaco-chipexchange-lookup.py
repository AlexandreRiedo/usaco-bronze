def verify(A, B, cA, cB, fA, nA, nB):
    return cA * ((B + nB) // cB) + (A + nA) >= fA


def solve(A, B, cA, cB, fA):
    init = ((B // cB) * cA) + A
    if init >= fA:
        return 0

    nB0 = cB - 1 - (B % cB)
    nA0 = fA - 1 - init

    if cA >= cB:
        i = 0
    else:
        i = nA0 // cA

    nA, nB = nA0 - cA * i, nB0 + i * cB

    return 1 + nA + nB


for _ in range(int(input())):
    A, B, cA, cB, fA = map(int, input().split())
    print(solve(A, B, cA, cB, fA))
