from collections import defaultdict

len_nums = int(input())
nums = list(map(int, input().split()))

freq = defaultdict(list)
for idx, num in enumerate(nums):
    freq[num].append(idx)

prefix = []
distinct = set()
for num in nums:
    prefix.append(len(distinct))
    distinct.add(num)

count = 0
for candidate, indices in freq.items():
    if len(indices) >= 2:
        count += prefix[indices[-2]]
        if len(indices) >= 3:
            count -= 1

print(count)