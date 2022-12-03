#include <bits/stdc++.h>
#define ll long long
using namespace std;

long long modinv(long long a, long long m)
{
    long long b = m, u = 1, v = 0;
    while (b)
    {
        long long t = a / b;
        a -= t * b;
        swap(a, b);
        u -= t * v;
        swap(u, v);
    }
    u %= m;
    if (u < 0)
        u += m;
    return u;
}

int main()
{
    ll N, P;
    cin >> N >> P;
    vector<ll> dp(N + 1);
    dp[0] = 0;
    dp[1] = 1; //
    ll MOD = 998244353;
    for (ll i = 2; i <= N; i++)
    {
        dp[i] = (P * (dp[i - 2] + 1) + (100 - P) * (dp[i - 1] + 1)) % MOD;
        dp[i] = dp[i] * modinv(100, MOD) % MOD;
    }
    cout << dp[N] << endl;
}