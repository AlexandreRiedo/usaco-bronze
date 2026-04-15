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

prior = [0, MAX_SENSOR_RANGE]
for ramp_presence, lower, upper in reversed(segments):
    lower, upper = min(lower, upper), max(lower, upper)

    if ramp_presence == "none":
        prior[0] = max(prior[0], lower)
        prior[1] = min(prior[1], upper)

    elif ramp_presence == "off":
        prior[0] = prior[0] + lower
        prior[1] = prior[1] + upper

    elif ramp_presence == "on":
        prior[0] = max(0, prior[0] - upper)
        prior[1] = max(0, prior[1] - lower)

after = [0, MAX_SENSOR_RANGE]
for ramp_presence, lower, upper in segments:
    lower, upper = min(lower, upper), max(lower, upper)

    if ramp_presence == "none":
        after[0] = max(after[0], lower)
        after[1] = min(after[1], upper)

    elif ramp_presence == "off":
        after[0] = max(0, after[0] - upper)
        after[1] = max(0, after[1] - lower)

    elif ramp_presence == "on":
        after[0] = after[0] + lower
        after[1] = after[1] + upper

print(" ".join(map(str, sorted(prior))))
print(" ".join(map(str, sorted(after))))

# BREAKING?
"""

"""

# EXPLORING THE AFTER CASES
"""
6 9
on 1 4
?

7 13 seems the best
"""

"""
6 9
off 1 3
?

3 8 seems the best
"""

# EXPLORING THE PRIOR CASES
"""
?
on 2 3
11 14

8 12 is the most specific

"""

"""
?
off 4 6
6 10

10 16 is the most specific
"""
