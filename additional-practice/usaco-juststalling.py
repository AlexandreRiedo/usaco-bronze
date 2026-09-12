def prod(a):
    ans = a[0]
    for num in a[1:]:
        ans *= num
    return ans


N = int(input())
cows = sorted(map(int, input().split()), reverse=True)
stalls = sorted(map(int, input().split()))

ans = []
for idx, c in enumerate(cows):
    ans.append(sum(c <= h for h in stalls) - idx)
print(prod(ans))
