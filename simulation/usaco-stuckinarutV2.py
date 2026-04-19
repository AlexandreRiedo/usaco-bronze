from math import inf

num_locations = int(input())
locations = []
result = [-1 for _ in range(num_locations)]
for index in range(num_locations):
    direction, x, y = input().split()
    locations.append(
        [int(x), int(y), direction, index, inf, inf]
    )  # last two for the ending xy positions

locations.sort(key=lambda x: x[0] + x[1], reverse=True)

for location in locations:
    if location[2] == "E":
        filtered = filter(
            lambda x: (
                x[2] == "N"
                and x[0] > location[0]
                and x[1] < location[1]
                and x[5] > location[1]
            ),
            locations,
        )
        for problem_location in filtered:
            if problem_location[0] - location[0] > location[1] - problem_location[1]:
                location[4] = min(location[4], problem_location[0])
                location[5] = location[1]
    elif location[2] == "N":
        filtered = filter(
            lambda x: (
                x[2] == "E"
                and x[0] <= location[0]
                and x[1] > location[1]
                and x[4] > location[0]
            ),
            locations,
        )
        for problem_location in filtered:
            if problem_location[0] - location[0] > location[1] - problem_location[1]:
                location[4] = location[0]
                location[5] = min(location[5], problem_location[1])

results = ["Infinity" for _ in range(num_locations)]
for location in locations:
    if location[2] == "E":
        if location[4] == inf:
            results[location[3]] = "Infinity"
        else:
            results[location[3]] = str(location[4] - location[0])
    elif location[2] == "N":
        if location[5] == inf:
            results[location[3]] = "Infinity"
        else:
            results[location[3]] = str(location[5] - location[1])

print("\n".join(results))

"""
6
E 3 5
N 5 3
E 4 6
E 10 4
N 11 2
N 8 1
"""

# TODO
"""
Get a new example and study it carefully
Solution without simulation?
"""
