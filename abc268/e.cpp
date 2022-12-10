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
    // iv ixがそれぞれ何を示しているのか？
    for (ll i = 0; i < N; i++)
    {
        auto j = (p[i] - i + N) % N;
        cout << j << "," << (j + N / 2 + 1) << "," << (N + j - (N - 1) / 2) << endl;
        iv[j] -= j;
        iv[j + N / 2 + 1] += j;
        iv[N + j - (N - 1) / 2] += N + j;
        iv[N + j] -= N + j;

        ix[j] += 1;
        ix[j + N / 2 + 1] -= 1;
        ix[N + j - (N - 1) / 2] -= 1;
        ix[N + j] += 1;
    }

    // コストの和を計算している。
    for (int i = 0; i < N * 2 - 1; i++)
    {
        iv[i + 1] += iv[i];
        ix[i + 1] += ix[i];
    }
    ll ans = 1000000000000000000;
    for (int i = 0; i < N; i++)
    {
        // modだから逆元かな
        ans = min(ans, iv[i] + iv[i + N] + ix[i] * i + ix[i + N] * (i + N));
    }
    cout << ans << endl;
}