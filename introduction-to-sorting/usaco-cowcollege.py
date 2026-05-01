num_cows = int(input())
tuitions = [int(item) for item in input().split()]
tuitions.sort()

prefix = []
for i in range(num_cows):
    prefix.append(((num_cows - i) * tuitions[i], tuitions[i]))

prefix.sort(key=lambda x: (-x[0], x[1]))
print(f"{prefix[0][0]} {prefix[0][1]}")
