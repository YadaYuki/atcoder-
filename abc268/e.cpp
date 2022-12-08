#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    ll N;
    cin >> N;
    vector<ll> p(N);
    for (ll i = 0; i < N; i++)
    {
        cin >> p[i];
    }

    vector<ll> iv(N * 2), ix(N * 2);

    for (ll i = 0; i < N; i++)
    {
        auto j = (p[i] - i + N) % N;
        iv[j] -= j;
        iv[j + N / 2 + 1] += j;
        ix[j] += 1;
        ix[j + N / 2 + 1] -= 1;
        iv[N + j - (N - 1) / 2] += N + j;
        iv[N + j] -= N + j;
        ix[N + j - (N - 1) / 2] -= 1;
        ix[N + j] += 1;
    }
    for (int i = 0; i < N * 2 - 1; i++)
    {
        iv[i + 1] += iv[i];
        ix[i + 1] += ix[i];
    }
    ll ans = 1000000000000000000;
    for (int i = 0; i < N; i++)
    {
        ans = min(ans, iv[i] + ix[i] * i + iv[i + N] + ix[i + N] * (i + N));
    }
    cout << ans << endl;
}