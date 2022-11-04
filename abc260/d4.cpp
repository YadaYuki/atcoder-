#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    ll N, K;
    cin >> N >> K;

    vector<ll> P(N);
    for (ll i = 0; i < N; i++)
    {
        cin >> P[i];
    }

    vector<ll> under(N + 1); // under[i] ... iの下にあるカード
    under.assign(N + 1, -1);
    
    vector<ll> piles(N + 1); // piles[i] ... iの下にあるカードの枚数 + 1
    
    vector<ll> ans(N+1);
    ans.assign(N+1, -1);

    set<ll> s;

    for (ll i = 0; i < N; i++)
    {
        auto p = P[i];
        auto iter = s.lower_bound(p);
        if (iter == s.end())
        {
            s.insert(p);
            piles[p] = 1;
        }
        else
        {
            auto val = *iter;
            s.erase(val);
            under[p] = val;
            piles[p] = piles[val] + 1;
            s.insert(p);
        }

        if (piles[p] == K)
        {
            // remove
            s.erase(p);
            while (p != -1)
            {
                ans[p] = i + 1;
                p = under[p];
            }
        }
    }
    for (ll i = 1; i <= N; i++)
    {
        cout << ans[i] << endl;
    }
}