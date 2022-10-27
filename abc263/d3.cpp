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

    // dp
    vector<ll> fl(N + 1, 0);
    for (int i = 1; i <= N; i++)
    {
        fl[i] = min(fl[i - 1] + A[i - 1], L * i);
    }

    vector<ll> fr(N + 1, 0);
    for (int i = N - 1; i >= 0; i--)
    {
        fr[i] = min(fr[i + 1] + A[i], R * (N - i));
    }
    ll ans = 5e18;
    for(int i=0;i<=N;i++){
        ans = min(ans,fl[i] + fr[i]);
    }
    cout << ans << endl;
}