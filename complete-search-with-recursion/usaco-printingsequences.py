def solve(ref_sequence: list):
    is_possible = False
    digits = set(ref_sequence)

    def backtrack(
        current_sequence: list = [],
        used_digits: set = set(),
    ):
        nonlocal is_possible
        print(f"{current_sequence=}")

        if current_sequence == ref_sequence:
            is_possible = True
            return

        if len(current_sequence) > len(ref_sequence):
            return
        
        # if len(current_sequence) != 0:
        #     to_copy = current_sequence.copy()
        #     original_len = len(current_sequence)
        #     for _ in range(len(ref_sequence)):
        #         current_sequence.extend(to_copy)
        #         backtrack(current_sequence, used_digits)
        #     current_sequence = current_sequence[0:original_len]


        for digit in digits:
            if digit in used_digits:
                continue

            used_digits.add(digit)

            extra_prints = len(ref_sequence) - len(current_sequence)
            for _ in range(extra_prints):
                current_sequence.append(digit)
                backtrack(current_sequence, used_digits)
            for _ in range(extra_prints):
                current_sequence.pop()

            used_digits.remove(digit)

    backtrack()

    return is_possible


num_tests = int(input())
for _ in range(num_tests):
    num_integers, max_num_print = map(int, input().split())
    sequence = list(map(int, input().split()))

    if len(set(sequence)) > max_num_print:
        print("NO")
    else:
        if solve(sequence):
            print("YES")
        else:
            print("NO")

"""
4
4 2
1 2 2 2
4 2
1 1 2 1
4 2
1 1 2 2
6 2
1 1 2 2 1 1
"""
