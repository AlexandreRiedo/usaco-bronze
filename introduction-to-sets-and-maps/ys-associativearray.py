from collections import defaultdict

num_queries = int(input())
queries = defaultdict(lambda: "0")

for _ in range(num_queries):
    op, *values = input().split()

    if op == "0":
        queries[values[0]] = values[1]
    elif op == "1":
        print(queries[values[0]])
