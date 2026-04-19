import sys

sys.stdin = open("pails.in", "r")
sys.stdout = open("pails.out", "w")

smallest_pail, medium_pail, m_pail = map(int, input().split())

max_milk = 0
for num_smallest_pails in range(0, 1 + (m_pail // smallest_pail)):
    curr_milk = num_smallest_pails * smallest_pail

    if curr_milk > m_pail:
        break

    num_medium_pails = (m_pail - curr_milk) // medium_pail
    curr_milk = curr_milk + (num_medium_pails * medium_pail)

    max_milk = max(max_milk, curr_milk)

print(max_milk)
