#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    ll N, X;
    cin >> N >> X;
    vector<pair<ll, ll>> stages;
    for (int i = 0; i < N; i++)
    {
        ll a, b;
        cin >> a >> b;
        stages.push_back(pair{a, b});
    }
    ll cost_base = 0;
    ll B_min = 1e10;
    ll ans = 5e18;
    for (int i = 0; i < N; i++)
    {
        auto stage = stages[i];
        ll A = stage.first;
        ll B = stage.second;
        cost_base += (A + B);
        B_min = min(B_min, B);
        ll total_cost = cost_base + (B_min * (X - (i + 1)));
        ans = min(ans, total_cost);
    }

    cout << ans << endl;
}