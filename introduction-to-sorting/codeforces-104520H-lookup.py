num_elements = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = [num * ((idx + 1) * (num_elements - idx)) for idx, num in enumerate(a)]
a.sort()
b.sort(reverse=True)

res = sum(num_a * num_b for num_a, num_b in zip(a, b))
print(res)
