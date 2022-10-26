#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    ll N, L, R;
    cin >> N >> L >> R;
    vector<ll> A(N);
    for (int i = 0; i < N; i++)
    {
        cin >> A[i];
    }

    vector<ll> fl(N + 1);
    vector<ll> fr(N + 1);

    fl[0] = 0;
    for (int i = 0; i < N; i++)
    {
        fl[i + 1] = min(fl[i] + A[i], L * (i + 1));
    }

    fr[N] = 0;
    for (int i = N - 1; i >= 0; i--)
    {
        fr[i] = min(fr[i + 1] + A[i], R * (N - i));
    }

    ll ans = 5e18;
    for (int i = 0; i <= N; i++)
    {
        ans = min(ans, fl[i] + fr[i]);
    }
    cout << ans << endl;
}