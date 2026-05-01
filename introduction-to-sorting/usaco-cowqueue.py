with open("cowqueue.in") as file:
    num_cows = int(file.readline())
    cows = []
    for _ in range(num_cows):
        time_arrival, time_needed = map(int, file.readline().split())
        cows.append((time_arrival, time_needed))
    cows.sort(key=lambda x: x[0])

time_passed = 0
for time_arrival, time_needed in cows:
    time_passed = max(time_passed, time_arrival)
    time_passed += time_needed

with open("cowqueue.out", "w") as file:
    file.write(f"{time_passed}")
