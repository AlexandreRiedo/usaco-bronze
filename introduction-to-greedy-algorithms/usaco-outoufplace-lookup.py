with open("outofplace.in") as f:
    num_cows = int(f.readline().strip())
    cows = [int(f.readline().strip()) for _ in range(num_cows)]
    sorted_cows = sorted(cows)

count = 0
for i in range(num_cows):
    if cows[i] != sorted_cows[i]:
        count += 1
count -= 1


with open("outofplace.out", "w") as f:
    f.write(f"{count}\n")
