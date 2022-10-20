#include <bits/stdc++.h>
#include <cmath>
#define ll long long
using namespace std;

bool is_squere(long long N)
{
    long long r = (long long)floor(sqrt((long double)N)); // 切り捨てした平方根
    return (r * r) == N;
}

int main()
{
    ll N;
    cin >> N;
    vector<vector<ll>> divisors(N + 1);
    for (ll i = 1; i <= N; i++)
    {
        for (ll j = 1; j * j <= i; j++)
        {
            if ((i % j) == 0)
            {
                divisors[i].push_back(j);
                if (j * j != i)
                {
                    divisors[i].push_back(i / j);
                }
            }
        }
        sort(divisors[i].begin(),divisors[i].end());
    }
    map<ll, ll> vals2cnt;
    for (ll i = 1; i <= N; i++)
    {
        ll fi = -1;
        for (auto divisor : divisors[i])
        {
            if (is_squere(divisor))
            {
                fi = divisor;
            }
        }
        ll val = i / fi;
        vals2cnt[val] += 1;
    }
    ll ans = 0;
    for (const auto &[key, value] : vals2cnt)
    {
        ans += value * value;
    }
    cout << ans << endl;
}