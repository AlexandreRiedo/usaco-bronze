import random


def local_solve(idx: int, s: list[str]) -> int:
    left_idx, right_idx = idx, idx
    while left_idx > 0 and s[left_idx - 1] == "A":
        left_idx -= 1
    while right_idx < len(s) - 1 and s[right_idx + 1] == "A":
        right_idx += 1

    left_score, right_score = abs(idx - left_idx), abs(idx - right_idx)
    if left_score >= right_score:
        s[left_idx : idx + 1] = "B" + "C" * left_score
        return left_score
    else:
        s[idx : right_idx + 1] = "C" * right_score + "B"
        return right_score


def solve(s):
    ans = 0
    for idx in range(len(s)):
        if s[idx] == "B" and (
            s[max(0, idx - 1)] == "A" or s[min(len(s) - 1, idx + 1)] == "A"
        ):
            ans += local_solve(idx, s)
    return ans


from rich import print as rprint

while True:
    s = [random.choice("AB") for _ in range(10)]

    rprint(f"[blue]{''.join(s)}")
    if (count := s.count("A")) != (ans := solve(s)):
        rprint(f"[red]{ans=} [yellow]{count=} [blue]{''.join(s)}")
        break


# for _ in range(int(input())):
#     s = list(input())
#     # s = [random.choice("AB") for _ in range(10)]
#     rprint("".join(s))

#     ans = 0
#     for idx in range(len(s)):
#         if s[idx] == "B" and (
#             s[max(0, idx - 1)] == "A" or s[min(len(s) - 1, idx + 1)] == "A"
#         ):
#             ans += local_solve(idx, s)
#     rprint(s, ans, "\n")
#     # print(ans)


"""
VIP : COUNTER-EXAMPLE OF MY IDEA
ABAABAABBA
BAA BAA BA
-> ACCBCCBBCB with 5

AB AAB AAB BA
-> BC BCC BCC CB with 6
---
BAABA
CBABA
CCBBA
CCBCB -> 3

BAABA
BABCA
BBCCA -> 2
---
BABA
CBBA
CBCB -> 2

BABA
BBCA -> 1
---
BAAAAB
CBAAAB
CCBAAB
CCCBAB
CCCCBB -> 4

BAAAAB
BAAABC
BAABCC
BABCCC
BBCCCC -> 4
---
AABAAAA
AACBAAA
AACCBAA
AACCCBA
AAACCCB -> 4

AABAAAA
ABCAAAA
BCCAAAA -> 2
---
BABAABB
CBBAABB
CBCBABB
CBCCBBB -> 3
---
BBABA

"""

"""
"".join([random.choice("AB") for _ in range(7)])
"""
