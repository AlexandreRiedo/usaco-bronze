GENOME_ID = {"A": 0, "T": 1, "C": 2, "G": 3}

with open("cownomics.in") as read:
	cow_num, genome_len = [int(i) for i in read.readline().split()]

	spotted = []
	for _ in range(cow_num):
		genome_str = read.readline()
		genome = []
		for g in range(genome_len):
			# A -> 0, C -> 1, T -> 2, G -> 3
			genome.append(GENOME_ID[genome_str[g]])
		spotted.append(genome)

	plain = []
	for _ in range(cow_num):
		genome_str = read.readline()
		genome = []
		for g in range(genome_len):
			genome.append(GENOME_ID[genome_str[g]])
		plain.append(genome)

valid_sets = 0
for a in range(genome_len):
	for b in range(a + 1, genome_len):
		for c in range(b + 1, genome_len):
			spotted_ids = [False for _ in range(64)]
			for sc in range(cow_num):
				total = spotted[sc][a] * 16 + spotted[sc][b] * 4 + spotted[sc][c] * 1
				spotted_ids[total] = True

			for pc in range(cow_num):
				total = plain[pc][a] * 16 + plain[pc][b] * 4 + plain[pc][c] * 1
				if spotted_ids[total]:
					break
			else:
				valid_sets += 1

print(valid_sets, file=open("cownomics.out", "w"))