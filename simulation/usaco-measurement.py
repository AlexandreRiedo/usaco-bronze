import sys

sys.stdin = open("measurement.in", "r")
sys.stdout = open("measurement.out", "w")

cows = {"Bessie": 7, "Mildred": 7, "Elsie": 7}
displayed = {"Bessie", "Mildred", "Elsie"}
num_measurements = int(input())
measurements = []
for _ in range(num_measurements):
    day, name, change = input().split()
    measurements.append((int(day), name, int(change)))
measurements.sort(key=lambda x: x[0])

display_changes = 0
for day, name, change in measurements:
    cows[name] += change

    new_displayed = set()
    max_value = max(cows.values())
    for cow, value in cows.items():
        if value == max_value:
            new_displayed.add(cow)

    if displayed != new_displayed:
        displayed = new_displayed
        display_changes += 1

print(display_changes)