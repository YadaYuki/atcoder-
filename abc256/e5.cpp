#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    ll N, M;
    cin >> N >> M;
    ll A, B, C, D, E, F;
    cin >> A >> B >> C >> D >> E >> F;
    set<pair<ll, ll>> obstructions;
    for (int i = 0; i < M; i++)
    {
        ll x, y;
        cin >> x >> y;
        obstructions.insert({x, y});
    }

    map<pair<ll, ll>, ll> dp;
    dp[{0, 0}] = 1;
    ll MOD = 998244353;
    for (int i = 0; i < N; i++)
    {
        map<pair<ll, ll>, ll> tmp_dp;
        for (auto [k, v] : dp)
        {
            ll x = k.first;
            ll y = k.second;
            vector<pair<ll, ll>> next = {{x + A, y + B}, {x + C, y + D}, {x + E, y + F}};
            for (auto n : next)
            {
                if (obstructions.find(n) != obstructions.end())
                {
                    continue;
                }
                tmp_dp[n] += v;
                tmp_dp[n] %= MOD;
            }
        }
        swap(tmp_dp, dp);
    }
    ll ans = 0;
    for (auto [k, v] : dp)
    {
        ans += v;
        ans %= MOD;
    }
    cout << ans << endl;
}