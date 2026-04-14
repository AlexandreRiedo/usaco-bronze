import sys

MAX_SENSOR_RANGE = 1000

sys.stdin = open("traffic.in", "r")
sys.stdout = open("traffic.out", "w")

num_miles = int(input())
segments = []
for _ in range(num_miles):
    ramp_presence, lower, upper = input().split()
    lower = int(lower)
    upper = int(upper)
    segments.append((ramp_presence, lower, upper))

prior = None
i = len(segments)
while prior is None:
    i -= 1
    if segments[i][0] == "none":
        prior = [segments[i][1], segments[i][2]]

for ramp_presence, lower, upper in reversed(segments[:i]):
    if ramp_presence == "none":
        prior[0] = max(prior[0], lower)
        prior[1] = min(prior[1], upper)

    if ramp_presence == "off":
        prior[0] = prior[0] + lower
        prior[1] = prior[1] + upper

    if ramp_presence == "on":
        prior[0] = prior[0] - upper
        prior[1] = prior[1] - lower


after = None
j = -1
while after is None:
    j += 1
    if segments[j][0] == "none":
        after = [segments[j][1], segments[j][2]]

for ramp_presence, lower, upper in segments[j + 1 :]:
    if ramp_presence == "none":
        after[0] = max(after[0], lower)
        after[1] = min(after[1], upper)

    if ramp_presence == "off":
        after[0] = after[0] - upper
        after[1] = after[1] - lower

    if ramp_presence == "on":
        after[0] = after[0] + lower
        after[1] = after[1] + upper

print(" ".join(map(str, prior)))
print(" ".join(map(str, after)))

# EXPLORING THE AFTER CASES
"""
6 9
on 1 4
?

10 10 is the most specific?
7 13 seems the best

"""

# EXPLORING THE PRIOR CASES
"""
?
on 2 3
11 14

9 11 is the most specific

"""

"""
?
off 4 6
6 10

12 14 is the most specific
"""
