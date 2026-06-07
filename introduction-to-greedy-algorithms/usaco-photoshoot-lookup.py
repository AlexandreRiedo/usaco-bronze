cow_num = int(input())
cows = input()
assert len(cows) == cow_num and cow_num % 2 == 0

flips = 0
for c in range(cow_num - 2, -1, -2):
	sub = cows[c : c + 2]
	if sub[0] == sub[1]:
		continue
	if (sub == "GH" and flips % 2 == 0) or (sub == "HG" and flips % 2 == 1):
		flips += 1

print(flips)