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
    ll MOD = 998244353;

    for (int i = 0; i < M; i++)
    {
        ll x, y;
        cin >> x >> y;
        obstructions.insert({x, y});
    }
    map<pair<ll, ll>, ll> dp;
    dp[{0, 0}] = 1;
    vector<pair<ll, ll>> moves = {{A, B}, {C, D}, {E, F}};
    for (int i = 0; i < N; i++)
    {
        map<pair<ll, ll>, ll> tmp_dp;
        for (auto [cur, paths_to_cur] : dp)
        {
            for (auto move : moves)
            {
                pair<ll, ll> nexts = {cur.first + move.first, cur.second + move.second};
                if (obstructions.find(nexts) != obstructions.end())
                {
                    continue;
                }
                tmp_dp[nexts] += paths_to_cur;
                tmp_dp[nexts] %= MOD;
            }
        }
        swap(dp, tmp_dp);
    }
    ll ans = 0;
    for (auto [cur, paths_to_cur] : dp)
    {
        ans += paths_to_cur;
        ans %= MOD;
    }
    cout << ans << endl;
}