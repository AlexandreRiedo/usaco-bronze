MAX_SIMULATION_DEPTH = 1_000

num_locations = int(input())
locations = []
result = [-1 for _ in range(num_locations)]
for _ in range(num_locations):
    direction, x, y = input().split()
    locations.append(
        [direction, int(x), int(y), int(x), int(y)]
    )  # [3] and [4] are for keeping the starting locations

to_ignore = set()
for _ in range(MAX_SIMULATION_DEPTH):
    for location in locations:
        if tuple(location) in to_ignore:
            continue

        if location[0] == "E":
            location[1] += 1
        elif location[0] == "N":
            location[2] += 1

    for east_location in filter(
        lambda x: x[0] == "E" and tuple(x) not in to_ignore, locations
    ):
        for north_location in filter(lambda x: x[0] == "N", locations):
            if (
                east_location[1] == north_location[1]
                and north_location[2] > east_location[2]
                and north_location[4] <= east_location[2]
            ):
                to_ignore.add(tuple(east_location))

    for north_location in filter(
        lambda x: x[0] == "N" and tuple(x) not in to_ignore, locations
    ):
        for east_location in filter(lambda x: x[0] == "E", locations):
            if (
                north_location[2] == east_location[2]
                and east_location[1] > north_location[1]
                and east_location[3] < north_location[1]
            ):
                to_ignore.add(tuple(north_location))

for res in to_ignore:
    if res[0] == "E":
        result[locations.index(list(res))] = res[1] - res[3]
    elif res[0] == "N":
        result[locations.index(list(res))] = res[2] - res[4]

for res in result:
    print(res if res != -1 else "Infinity")

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
