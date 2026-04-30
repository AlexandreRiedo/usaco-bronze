import sys

num_values = int(sys.stdin.readline().rstrip())
values = set(map(int, sys.stdin.readline().rstrip().split()))
print(len(values))
