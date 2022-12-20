#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N;
    cin >> N;
    //

    ll ok = 1;
    ll ng = N + 1;
    while (ng - ok > 0)
    {
        ll mid = (ok + ng) / 2;
        ll a = ok;
        ll b = mid;
        ll c = 1;
        ll d = N;
        cout << "? " << a << " " << b << " " << c << " " << d << endl;
        ll T;
        cin >> T;
        if (T == (b - a + 1))
        {
            ok = mid + 1;
        }
        else
        {
            ng = mid;
        }
    }
    auto u = ok;
    ok = 1;
    ng = N + 1;
    while (ng - ok > 0)
    {
        ll mid = (ok + ng) / 2;
        ll a = 1;
        ll b = N;
        ll c = ok;
        ll d = mid;
        cout << "? " << a << " " << b << " " << c << " " << d << endl;
        ll T;
        cin >> T;
        if (T == (d - c + 1))
        {
            ok = mid + 1;
        }
        else
        {
            ng = mid;
        }
    }
    auto l = ok;
    cout << "! " << u << " " << l << endl;
}