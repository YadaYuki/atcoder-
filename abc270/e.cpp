#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    ll N, K;
    cin >> N >> K;
    vector<ll> A(N);
    for (ll i = 0; i < N; i++)
    {
        cin >> A[i];
    }
    //
    ll ok = 1000000000001;
    ll ng = -1;
    while (ok - ng > 1)
    {
        auto mid = (ok + ng) / 2;
        auto k = K;
        for (auto a : A)
        {
            k -= min(a, mid);
        }
        if (k <= 0)
        {
            ok = mid;
        }
        else
        {
            ng = mid;
        }
    }

    auto total_rotate_cnt = ok;
    for (int i = 0; i < N; i++)
    {
        auto c = min(total_rotate_cnt - 1, A[i]);
        A[i] -= c;
        K -= c;
    }

    for (int i = 0; i < N; i++)
    {
        auto c = min(1LL, A[i]);
        A[i] -= c;
        K -= c;
        if (K <= 0)
        {
            break;
        }
    }
    for (int i = 0; i < N; i++)
    {
        cout << A[i] << " ";
    }
    cout << endl;
}