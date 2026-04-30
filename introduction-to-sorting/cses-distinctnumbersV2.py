import sys

num_values = int(sys.stdin.readline().rstrip())
values = set(sys.stdin.readline().rstrip().split())
print(len(values))
