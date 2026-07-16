n = int(input())
a = [int(x) - 1 for x in input().split()]
b = [int(x) - 1 for x in input().split()]

moved = [0] * n
j = res = 0


for i in range(n):
	while j < n and moved[a[j]]:
		j += 1

	if a[j] == b[i]:
		j += 1
	else:
		res += 1
		moved[b[i]] = 1


print(res)