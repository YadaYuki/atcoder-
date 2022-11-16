#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    ll N;
    cin >> N;
    map<ll, pair<ll, ll>> L; // a_0 ~ a_Nまでの最小公倍数
    vector<map<ll, ll>> a(N);
    for (ll i = 0; i < N; i++)
    {
        ll m;
        cin >> m;
        for (ll j = 0; j < m; j++)
        {
            ll p, e;
            cin >> p >> e;
            a[i][p] = e;
            // Lを作成
            // https://stackoverflow.com/questions/1939953/how-to-find-if-a-given-key-exists-in-a-c-stdmap
            if (L.find(p) == L.end())
            {
                L[p] = pair<ll, ll>{e, 1LL};
            }
            else
            {
                if (L[p].first < e)
                {
                    L[p] = pair<ll, ll>{e, 1LL};
                }
                else if (L[p].first == e)
                {
                    L[p].second += 1;
                }
            }
        }
    }

    ll ans = 0;
    for (ll i = 0; i < N; i++)
    {
        auto ai = a[i];
        for (auto [p, e] : ai)
        {
            if (L[p].first == e && L[p].second == 1)
            {
                ans += 1;
                break;
            }
        }
    }

    ans = ans + min(1LL, N - ans);
    cout << ans << endl;
}
