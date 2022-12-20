#include <bits/stdc++.h>
using namespace std;

int main()
{

    int N;
    cin >> N;

    vector<int> p(N);

    for (int i = 0; i < N; i++)
        cin >> p[i];

    vector<long long> iv(N * 2), ix(N * 2);

    for (int i = 0; i < N; i++)
    {

        int j = (p[i] - i + N) % N;
        cout << j << "," << i << "," << p[i] << endl;
        // iの不満が0になるような回転数
        iv[j] -= j;
        iv[j + N / 2 + 1] += j;
        iv[N + j - (N - 1) / 2] += N + j;
        iv[N + j] -= N + j;

        ix[j] += 1;
        ix[j + N / 2 + 1] -= 1;
        ix[N + j - (N - 1) / 2] -= 1;
        ix[N + j] += 1;
    }

    for (int i = 0; i < N * 2 - 1; i++)
    {
        iv[i + 1] += iv[i];
        ix[i + 1] += ix[i];
    }

    long long ans = 1000000000000000000;
    for (int x = 0; x < N; x++)
    {
        ans = min(ans, iv[x] + ix[x] * x + iv[x + N] + ix[x + N] * (x + N));
    }

    cout << ans << endl;

    return 0;
}
