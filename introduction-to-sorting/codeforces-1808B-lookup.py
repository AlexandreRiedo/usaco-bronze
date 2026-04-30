from collections import defaultdict

for _ in range(int(input())):
	deck_num, card_num = map(int, input().split())
	matrix = []
	for _ in range(deck_num):
		matrix.append(list(map(int, input().split())))

	# Group columns using a dictionary
	hashmap = defaultdict(list)
	for i in range(deck_num):
		for j in range(card_num):
			hashmap[j].append(matrix[i][j])

	total_res = 0
	for i in range(card_num):
		temp = sorted(hashmap[i], reverse=True)
		suf = []
		prev = 0
		for i in reversed(temp):
			suf.append(prev)
			prev += i

		col_res = 0
		for i in range(deck_num):
			col_res += temp[i] * (deck_num - i - 1) - suf[deck_num - i - 1]
		total_res += col_res

	print(total_res)