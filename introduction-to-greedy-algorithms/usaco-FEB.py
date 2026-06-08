from rich import print as rprint

num_texts = int(input())
conversation = list(input())


def count_score(conversation):
    score = 0
    for a, b in zip(range(len(conversation)), range(1, len(conversation))):
        char_a, char_b = conversation[a], conversation[b]
        if char_a == char_b and char_a != "F":  # guard
            score += 1
    return score


def rec_wrapper(conversation):
    scores = set()

    trace = []

    def rec(conversation, idx):
        if idx == len(conversation):
            score = count_score(conversation)
            scores.add(score)
            trace.append(("".join(conversation), score))
        else:
            if conversation[idx] != "F":
                rec(conversation, idx + 1)
            else:
                conversation[idx] = "B"
                rec(conversation, idx + 1)
                conversation[idx] = "E"
                rec(conversation, idx + 1)
                conversation[idx] = "F"

    idx = 0
    rec(conversation, idx)

    trace.sort(key=lambda x:(x[1], x[0]))
    for convo, score in trace:
        rprint(f"{convo} {score=}")

    return list(sorted(scores))


solutions = rec_wrapper(conversation)
print(len(solutions))
for ans in solutions:
    print(ans)

"""
PATTERN: FFX
FFE FFB
-> scores 2, or scores 1, or scores 0

PATTERN: XFF
EFF BFF
-> scores 2, or scores 1, or scores 0

PATTERN:
XF
-> Scores 1, 0

FX
-> Scores 1, 0
"""

"""
PATTERN: FF

FF
-> 0,1

FFF
-> 0,1,2

FFFF
-> 0,1,2,3

FFFFF
-> 0,1,2,3,4

FFFFFFFFFFF (11)
-> 0,1,2,3,4,5,6,7,8,9,10
"""

"""
PATTERN: XFX

4
EFFE -> 1 or 3

5
EFFFE -> 0, 2, or 4

6
EFFFFE -> 1, 3, 5

7
EFFFFFE -> 0, 2, 4, 6
"""

"""
PATTERN: XFY

3
EFB -> 1

4
EFFB -> 0, 2

5
EFFFB -> 1, 3

6
EFFFFB -> 0, 2, 4

7
EFFFFFB -> 1, 3, 5
"""

"""
EXPLORING
7
EFEEFEE -> 2+ 2+2, 2+ 2+0, 2+ 0+0

8
EFBEBBBE -> 2+ 1, 2+ 1

8
EFFFBBFF -> 1+ 1+2, 1+ 3+2, 1+ 1+1, 1+ 3+1, 1+ 1+0, 1+ 3+0
-> 6, 5, 4, 3, 2

10
BFFFFFEBFE ->
5, 3, 1
+ 1
-> 6, 4, 2

10
BFEFBFEFBF
  1
+ 1
+ 1
+ 1
+ 1, 0

NOTE: BFE or EFB can be counted as +1 automatically
"""

"""
10
BFFFFFEBFE -> 
+ 2, 1, 0
+ 2, 1, 0
"""


"""
CASEWORK
FX...
FFFF...
XFFF...

...XFFF
...FFFF
...X

XFFF...X
XFFF...Y
"""