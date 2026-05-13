with open("breedflip.in") as file:
    num_cows = int(file.readline())
    desired = file.readline()
    current = file.readline()

dif_streak = False
count = 0
for a, b in zip(desired, current):
    if a != b:
        if not dif_streak:
            count += 1
        dif_streak = True
    elif a == b:
        dif_streak = False

with open("breedflip.out", "w") as file:
    file.write(str(count))
