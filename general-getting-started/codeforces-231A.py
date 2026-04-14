num_problems = int(input())

print(sum([1 if sum(list(map(int, input().split()))) >= 2 else 0 for _ in range(num_problems)]))