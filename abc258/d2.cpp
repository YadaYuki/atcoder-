#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N, X;
    cin >> N >> X;
    vector<pair<ll, ll>> AB;
    for (int i = 0; i < N; i++)
    {
        ll a, b;
        cin >> a >> b;
        AB.push_back(pair{a,b});
    }

    ll ans = 5e18;
    ll cost_base = 0;
    ll B_min = 1e9 + 1;
    for(int i=0;i<N;i++){
        auto ab = AB[i];
        ll a = ab.first;
        ll b = ab.second;
        cost_base += a + b;
        B_min = min(B_min,b);
        int stg = i+1;
        ans = min(ans,cost_base + B_min * (X-stg));
    }
    cout << ans << endl;
}