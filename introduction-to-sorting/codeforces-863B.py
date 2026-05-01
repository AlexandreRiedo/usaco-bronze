import itertools

n = int(input())
num_people = 2 * n
num_tandems = n - 1
num_single = 2
weights = sorted(list(map(int, input().split())))

instability = []
for single_a_idx, single_b_idx in itertools.combinations(range(len(weights)), 2):
    candidate_instability = 0
    candidate_weights = [
        weight
        for idx, weight in enumerate(weights)
        if idx not in {single_a_idx, single_b_idx}
    ]
    for i in range(0, len(candidate_weights), 2):
        candidate_instability += abs(candidate_weights[i] - candidate_weights[i + 1])

    instability.append((candidate_instability, single_a_idx, single_b_idx))
instability.sort(key=lambda x: x[0])
min_value = instability[0][0]

print(min_value)
