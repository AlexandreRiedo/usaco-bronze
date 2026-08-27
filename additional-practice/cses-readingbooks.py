n = int(input())
times = list(map(int, input().split()))

M = max(times)
S = sum(times) - M

if S >= M:
    print(S + M)
else:
    print(M - S)

"""
Claude's Hint

Think about the longest book, M, 
and the sum of all the rest, S. 

Kotivalo spends a solid block 
of M time on that book; 
during that block Justiina can 
only be reading the other books. 

Ask yourself: what happens 
when S is big enough to cover that block, 
versus when it isn't? 
Those two cases give two different lower bounds, 
and each is achievable.
"""
