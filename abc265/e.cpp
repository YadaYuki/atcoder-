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
    for (ll i = 0; i < M; i++)
    {
        ll x, y;
        cin >> x >> y;
        obstructions.insert({x, y});
    }
    ll MOD = 998244353;
    map<pair<ll, ll>, ll> dp;
    dp[pair<ll, ll>{0, 0}] = 1;
    vector<pair<ll, ll>> dxy = vector<pair<ll, ll>>{
        {A, B},
        {C, D},
        {E, F},
    };
    for (int i = 0; i < N; i++)
    {
        map<pair<ll, ll>, ll> tmp_dp;

        for (auto [coordinate, cnt_of_path] : dp)
        {
            auto x = coordinate.first;
            auto y = coordinate.second;

            for (auto [dx, dy] : dxy)
            {
                auto n = pair<ll, ll>{x + dx, y + dy};
                auto n_is_not_obstruction = obstructions.find(n) == obstructions.end();
                if (n_is_not_obstruction)
                {
                    tmp_dp[n] += cnt_of_path;
                    tmp_dp[n] %= MOD;
                }
            }
        }
        swap(dp, tmp_dp);
    }
    ll ans = 0;
    for (auto [k, v] : dp)
    {
        ans += v;
        ans %= MOD;
    }
    cout << ans << endl;
}