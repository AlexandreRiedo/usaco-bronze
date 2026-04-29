import operator
from collections.abc import Callable

NUM_CARDS = 4
MAX = 24


def permutate_operators(
    operators: list[Callable] = [],
    result=set(),
):
    if len(operators) == 3:
        result.add(tuple(operators))
    else:
        for op in (operator.add, operator.sub, operator.mul, operator.truediv):
            operators.append(op)
            permutate_operators(operators, result)
            operators.pop()

    return result


OPERATOR_PERMUTATIONS = permutate_operators()


def calculate(card_hand: list[int], operators: list[Callable]):
    a, b, c, d = card_hand
    op1, op2, op3 = operators

    calculate = 0
    for idx, op_idx in enumerate(range(3)):
        if idx == 0:
            calculate = operators[op_idx](a, b)
        else:
            calculate = operators[op_idx](calculate, card_hand[idx + 1])

        if int(calculate) != calculate:
            calculate = 0
            break
    if calculate > 24:
        calculate = 0

    calculate_bis = 0
    temp1, temp2 = op1(a, b), op3(c, d)
    if int(temp1) == temp1 and int(temp2) == temp2 and temp2 != 0:
        calculate_bis = op2(temp1, temp2)
    if int(calculate_bis) != calculate_bis or calculate_bis > 24:
        calculate_bis = 0

    return max(int(calculate), int(calculate_bis))


num_card_hands = int(input())
for _ in range(num_card_hands):
    card_hand = [int(input()) for _ in range(NUM_CARDS)]

    def solve(
        card_hand: list[int],
        current_permutation: list[int] = [],
        used_indices: set[int] = set(),
        max_value=[0],
    ):
        if len(current_permutation) == 4:
            for operators in OPERATOR_PERMUTATIONS:
                max_value[0] = max(
                    calculate(current_permutation, operators), max_value[0]
                )
        else:
            for idx, card in enumerate(card_hand):
                if idx in used_indices:
                    continue

                current_permutation.append(card)
                used_indices.add(idx)
                solve(card_hand, current_permutation, used_indices, max_value)
                used_indices.remove(idx)
                current_permutation.pop()

        return max_value[0]

    print(solve(card_hand))


"""
((A + B) + C) + D
(A + B) + (C + D)
A + (B + C) + D
A + (B + C + D)
"""
