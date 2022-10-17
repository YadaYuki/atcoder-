#include <bits/stdc++.h>
using namespace std;
#define ll long long

// vector<ll> Hash, Pow;
ll MOD = 1e9 + 7;

ll char_2_num(char a)
{
    return a - 'a' + 1;
}

ll hash_i2j(ll i, ll j, ll Hash[], ll Pow[])
{
    if (i == 0)
    {
        return Hash[j];
    }
    auto word_cnt = j - i + 1;
    ll ans = (Hash[j] - Hash[i - 1] * Pow[word_cnt]) % MOD;
    if (ans < 0)
        ans += MOD;
    return ans;
}

int main()
{
    ll N, Q;
    cin >> N >> Q;
    string S;
    cin >> S;
    ll Hash[N];     // Hash[i] = Hash of S[0..i-1]
    ll Pow[N + 1];  // Pow[i] = L^i
    ll redix = 100; // A ~ Zまでを異なる整数で表現してくれる。

    Hash[0] = char_2_num(S.at(0));
    for (ll i = 1; i < N; i++)
    {
        Hash[i] = (redix * Hash[i - 1] + char_2_num(S.at(i))) % MOD;
    }
    Pow[0] = 1;
    for (ll i = 1; i <= N; i++)
    {
        Pow[i] = (Pow[i - 1] * redix % MOD);
    }

    // for (ll i = 0; i < N; i++)
    // {
    //     cout << Hash[i] << " ";
    // }
    // cout << endl;

    for (ll i = 1; i <= Q; i++)
    {
        ll a, b, c, d;
        cin >> a >> b >> c >> d;
        a--;
        b--;
        c--;
        d--;
        auto hash_a2b = hash_i2j(a, b, Hash, Pow);
        auto hash_c2d = hash_i2j(c, d, Hash, Pow);
        if (hash_a2b == hash_c2d)
        {
            cout << "Yes" << endl;
        }
        else
        {
            cout << "No" << endl;
        }
    }
}