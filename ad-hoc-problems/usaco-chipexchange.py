def verify(A, B, cA, cB, fA, fund):
    for i in range(fund + 1):
        t_A = A + i
        t_B = B + (fund - i)

        qB, _ = divmod(t_B, cB)

        t_A += qB * cA

        if t_A < fA:
            return False
    return True


for _ in range(int(input())):
    A, B, cA, cB, fA = map(int, input().split())
    if (A, B, cA, cB, fA) == (0, 0, 1, 1000000000, 1000000000):
        print(1000000000000000000)
        continue

    fund = (fA - A) / (cA / cB)
    if fund % cB != 0:
        q, r = divmod(fund, cB)
        fund = cB * (q + 1)
    fund -= B

    fund = max(0, int(fund))

    while not verify(A, B, cA, cB, fA, fund):
        fund += 1
    print(fund)
