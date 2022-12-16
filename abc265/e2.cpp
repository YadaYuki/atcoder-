#include <bits/stdc++.h>
#include <iterator>
#define ll long long
using namespace std;

int main()
{
    int N, M;
    cin >> N >> M;
    set<pair<ll, ll>> obstructions;
    ll A, B, C, D, E, F;
    cin >> A >> B >> C >> D >> E >> F;
    for (ll i = 0; i < M; i++)
    {
        ll x, y;
        cin >> x >> y;
        obstructions.insert({x, y});
    }
    map<pair<ll, ll>, ll> dp;
    dp[{0, 0}] = 1;
    ll MOD = 998244353;
    for (ll i = 0; i < N; i++)
    {
        map<pair<ll, ll>, ll> temp_dp;
        for (auto [c, paths] : dp)
        {
            vector<pair<ll, ll>> nexts = {{c.first + A, c.second + B},
                                          {c.first + C, c.second + D},
                                          {c.first + E, c.second + F}};
            for (auto n : nexts)
            {
                if (obstructions.find(n) != obstructions.end())
                {
                    continue;
                }
                temp_dp[n] += paths;
                temp_dp[n] %= MOD;
            }
        }
        swap(dp, temp_dp);
    }
    ll ans = 0;
    for (auto [k, v] : dp)
    {
        ans += v;
        ans %= MOD;
    }
    cout << ans << endl;
}