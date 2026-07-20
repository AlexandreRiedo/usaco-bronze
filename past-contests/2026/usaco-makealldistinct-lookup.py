import sys

def main():
    data = sys.stdin.buffer.read().split()
    pos = 0
    T = int(data[pos]); pos += 1
    out = []

    for _ in range(T):
        N = int(data[pos]); K = int(data[pos + 1]); pos += 2
        cnt = [0] * N
        for j in range(N):
            cnt[int(data[pos + j]) - 1] += 1
        pos += N

        if K < 0:
            cnt.reverse()   # a -> N+1-a, mirrors the count array
            K = -K

        ans = 0
        for i in range(K):              # residue class i mod K
            cur = i
            carry = 0                   # elements pushed up from lower slots
            while cur < N or carry > 0:
                if cur < N:
                    carry += cnt[cur]
                if carry > 0:
                    ans += carry - 1    # all but one must move up
                    carry -= 1          # one stays here
                cur += K
            # note: the decrement above only happens when carry > 0,
            # matching "leave one element at this slot"
        out.append(str(ans))

    print("\n".join(out))

main()