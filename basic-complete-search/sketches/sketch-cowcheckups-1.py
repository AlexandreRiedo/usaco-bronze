"""
IDEA: l-1 r+1 keeps the same middle structure
1 2 3 4 5 6 7 8 9
1 2 5 4 3 6 7 8 9 (vet_order)
1 2 3 4 5 6 7 8 9 (l4 r4)
1 2 5 4 3 6 7 8 9 (l3 r5)
1 6 5 4 3 2 7 8 9 (l2 r6)
7 6 5 4 3 2 1 8 9 (l1 r7)


1 2 3 4 5 6 7 8 9
1 2 6 5 4 3 7 8 9 (l3 r6)
1 7 6 5 4 3 2 8 9 (l2 r7)

TODO: Find the way to generate all possible lx rx values using this strategy.
"""

"""
VALUES TO TEST:
[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), 
(2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), 
(3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), 
(4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), 
(5, 5), (5, 6), (5, 7), (5, 8), (5, 9), 
(6, 6), (6, 7), (6, 8), (6, 9), 
(7, 7), (7, 8), (7, 9), 
(8, 8), (8, 9), 
(9, 9)]
"""

test_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test = [1, 3, 2, 2, 1, 3, 2]
test_d = [1, 2, 3]
test_c = list(range(1, 100 + 1))
LEN = len(test)
tuples_to_test = []

for left in range(1, 1 + LEN):
    for right in range(left, 1 + LEN):
        tuples_to_test.append((left, right))


def get_expansion_tuples(values, index, offset):
    left = index
    right = index + offset
    tuples_found = [(left - 1, right - 1)]
    expansion = 0
    while left - expansion > 1 and right + expansion <= len(values) - 1:
        expansion += 1
        tuples_found.append((left - 1 - expansion, right - 1 + expansion))
    return tuples_found


tuples_to_find = [(LEN, LEN)]
count = 1
cases = 1
print("SINGLE")
OFFSET_SINGLE = 0
for i in range(1, LEN):
    print(get_expansion_tuples(test, i, OFFSET_SINGLE))
    count += len(get_expansion_tuples(test, i, OFFSET_SINGLE))
    cases += 1
    for val in get_expansion_tuples(test, i, OFFSET_SINGLE):
        tuples_to_find.append(val)

print("")
print("DOUBLE")
OFFSET_DOUBLE = 1
for i in range(1, LEN):
    print(get_expansion_tuples(test, i, OFFSET_DOUBLE))
    count += len(get_expansion_tuples(test, i, OFFSET_DOUBLE))
    cases += 1
    for val in get_expansion_tuples(test, i, OFFSET_DOUBLE):
        tuples_to_find.append(val)

print("")
print("ANSWER")
print(f"Found length: {count}\nActual length: {len(tuples_to_test)}")
print(f"Cases to loop over: {cases}")
