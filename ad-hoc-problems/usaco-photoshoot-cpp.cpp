// CLAUDE's translation of my python code. This passes, but my python does not.

#include <bits/stdc++.h>
using namespace std;

int main() {
    long long N, K;
    cin >> N >> K;
    long long Q;
    cin >> Q;

    vector<vector<long long>> cows(N, vector<long long>(N, 0));
    vector<long long> photos((N - K + 1) * (N - K + 1), 0);
    long long ans = 0;

    for (long long q = 0; q < Q; q++) {
        long long r, c, v;
        cin >> r >> c >> v;
        r -= 1;
        c -= 1;
        v -= 1;

        for (long long y = max(0LL, r - K + 1); y < min(N - K, r) + 1; y++) {
            for (long long x = max(0LL, c - K + 1); x < min(N - K, c) + 1; x++) {
                photos[x + y * (N - K + 1)] += v + 1 - cows[r][c];
                ans = max(photos[x + y * (N - K + 1)], ans);
            }
        }
        cows[r][c] = v + 1;

        cout << ans << "\n";
    }

    return 0;
}