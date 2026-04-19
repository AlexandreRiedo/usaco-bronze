import sys
from collections import defaultdict
from typing import NamedTuple


class Record(NamedTuple):
    time: int
    cow_a: int
    cow_b: int


sys.stdin = open("tracing.in", "r")
sys.stdout = open("tracing.out", "w")

num_cows, num_records = map(int, input().split())
cow_states = {index + 1 for index, char in enumerate(input()) if char == "1"}
records = []
for _ in range(num_records):
    records.append(Record(*map(int, input().split())))
records.sort()

candidates = set()
possible_k = []

for k in range(0, num_records + 1):
    for patient_zero in range(1, num_cows + 1):
        infected = defaultdict(int)
        infected[patient_zero] = k

        for record in records:
            if record.cow_a in infected and record.cow_b in infected:
                infected[record.cow_a] = max(0, infected[record.cow_a] - 1)
                infected[record.cow_b] = max(0, infected[record.cow_b] - 1)
            elif record.cow_a in infected and infected[record.cow_a] > 0:
                infected[record.cow_a] -= 1
                infected[record.cow_b] = k
            elif record.cow_b in infected and infected[record.cow_b] > 0:
                infected[record.cow_b] -= 1
                infected[record.cow_a] = k

        if cow_states == set(infected.keys()):
            candidates.add(patient_zero)
            possible_k.append(k)

print(
    f"{len(candidates)} {possible_k[0]} {possible_k[-1] if possible_k[-1] != (num_records) else 'Infinity'}"
)
