#include <bits/stdc++.h>
#define ll long long
using namespace std;

map<ll, ll> prime_factorization(ll n)
{
    map<ll, ll> mp = {};
    while (n % 2 == 0)
    {
        n /= 2;
        mp[2L] += 1;
    }
    for (ll i = 3; i * i <= n; i += 2)
    {
        while (n % i == 0)
        {
            mp[i] += 1;
            n /= i;
        }
    }
    if(n!=1){
        mp[n] = 1;
    }
    return mp;
}

int main()
{
    ll K;
    cin >> K;
    auto pf = prime_factorization(K);
    ll ans = -1;
    
    for (auto [p, e] : pf)
    {
        for (ll n = p; true; n += p)
        {
            ll cnt = 0;
            auto v = n;
            while (v % p == 0)
            {
                cnt += 1;
                v /= p;
            }
            e -= cnt;
            if (e <= 0)
            {
                ans = max(ans, n);
                break;
            }
        }
    }
    cout << ans << endl;
}