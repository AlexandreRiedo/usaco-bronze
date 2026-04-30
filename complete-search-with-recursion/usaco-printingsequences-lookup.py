def solve1(l):
    if len(l) == 0:
        return True
    return min(l) == max(l)


def solve2(l):
    if solve1(l):
        return True
    r = 0
    blocks = []
    while r < len(l):
        i = r
        while r < len(l) and l[r] == l[i]:
            r += 1
        blocks.append((r - i, l[i]))
    return len(blocks) % 2 == 0 and blocks[2:] == blocks[:-2]


def solve3(l):
    for i in range(1, len(l) + 1):
        if len(l) % i == 0:
            if l[:-len(l) // i] == l[len(l) // i:]:
                substring = l[:len(l) // i]
                for i in range(len(substring) + 1):
                    if solve2(substring[:i]) and solve1(substring[i:]):
                        return True
                    if solve1(substring[:i]) and solve2(substring[i:]):
                        return True


def solve():
    N, K = map(int, input().split())
    seq = list(map(int, input().split()))
    if K == 1:
        return solve1(seq)
    elif K == 2:
        return solve2(seq)
    else:
        assert K == 3
        return solve3(seq)


T = int(input())
for _ in range(T):
    print("YES" if solve() else "NO")