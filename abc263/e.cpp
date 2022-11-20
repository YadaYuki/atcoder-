#include <bits/stdc++.h>
#define ll long long
using namespace std;

class SegmentTree
{
private:
    vector<ll> data;
    ll size;

    ll dfs(ll l, ll r, ll cl, ll cr, ll cur_idx)
    {
        auto is_in = (l <= cl) && (cr <= r);
        auto is_out = (cr <= l) || (r <= cl);
        if (is_in)
        {
            return data[cur_idx];
        }
        if (is_out)
        {
            return 0;
        }
        auto mid = (cl + cr) / 2;
        auto left_sum = dfs(l, r, cl, mid, cur_idx * 2);
        auto right_sum = dfs(l, r, mid, cr, cur_idx * 2 + 1);
        return left_sum + right_sum;
    }

public:
    explicit SegmentTree(ll n)
    {
        size = 1;
        while (n > size)
        {
            size *= 2;
        }
        data.assign(size * 2, 0);
    }

    void print_data()
    {
        for (int i = size; i < size * 2; i++)
        {
            cout << data[i] << " ";
        }
        cout << endl;
    }

    void update(ll pos, ll x)
    {
        data[pos + size - 1] = x;
        ll node_idx = pos + size - 1;
        while (node_idx > 0)
        {
            node_idx /= 2;
            data[node_idx] = data[node_idx * 2] + data[node_idx * 2 + 1];
        }
    }

    ll rsq(ll l, ll r)
    {
        return dfs(l, r, 1, size + 1, 1);
    }
};
// https://qiita.com/drken/items/3b4fdf0a78e7a138cd9a#3-2-mod-p-%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E9%80%86%E5%85%83 ... 知らなかった...難しい笑。
long long modinv(long long a, long long m) {
    long long b = m, u = 1, v = 0;
    while (b) {
        long long t = a / b;
        a -= t * b; swap(a, b);
        u -= t * v; swap(u, v);
    }
    u %= m;
    if (u < 0) u += m;
    return u;
}

// https://atcoder.jp/contests/abc263/submissions/36375937
int main()
{
    ll N;
    ll MOD = 998244353;
    cin >> N;
    vector<ll> A(N + 1);
    for (int i = 1; i <= N - 1; i++)
    {
        cin >> A[i];
    }
    vector<ll> dp(N + 1, 0);
    auto st = SegmentTree(N);
    st.update(N, 0);
    for (ll i = N - 1; i >= 1; i--)
    {
        auto r = (i + A[i]) % MOD;
        dp[i] = (st.rsq(i, r + 1) + MOD + A[i] + 1) % MOD;
        dp[i] = dp[i] * modinv(A[i], MOD) % MOD;
        st.update(i, dp[i]);
    }
    cout << dp[1] << endl;
}

