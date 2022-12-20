#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N, M;
    cin >> N >> M;
    vector<vector<int>> imos(N + 10, vector<int>(N + 10));
    for (int i = 0; i < M; i++)
    {
        int a, b, x;
        cin >> a >> b >> x;
        imos[a][b] += 1;
        imos[a][b+1] -= 1;
        imos[a + x + 1][b] -= 1;
        imos[a + x + 1][b + x + 1] += 1;
    }

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            cout << imos[i][j] << " ";
        }
        cout << endl;
    }
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            imos[i][j] = imos[i][j] + imos[i-1][j-1];
            imos[i][j] = imos[i][j] + imos[i-1][j];
        }
    }
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            cout << imos[i][j] << " ";
        }
        cout << endl;
    }
    int ans = 0;
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            ans += (imos[i][j] > 0);
        }
    }
    cout << ans << endl;
}