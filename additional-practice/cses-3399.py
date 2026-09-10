"""
Rotating an array:
https://codeanddebug.in/blog/rotate-an-array-by-k-places/#14-2-better-solution-using-slicing
"""

for _ in range(int(input())):
    n, a, b = map(int, input().split())

    if a == n or b == n or a + b > n or (a == 0 and b != 0) or (a != 0 and b == 0):
        print("NO")
    else:
        eq = n - (a + b)
        a_cards, b_cards = list(range(1, n + 1)), list(range(1, n + 1))

        if a == 0 and b == 0:
            pass
        elif a > b:
            a_cards[eq:] = a_cards[-a:] + a_cards[eq:-a]
        else:
            b_cards[eq:] = b_cards[-b:] + b_cards[eq:-b]

        print("YES")
        print(*a_cards)
        print(*b_cards)
