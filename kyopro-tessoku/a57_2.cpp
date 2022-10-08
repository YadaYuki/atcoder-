#include <bits/stdc++.h>
using namespace std;

int main()
{
    int N, Q;
    cin >> N >> Q;
    int A[N];
    for (int i = 0; i < N; i++)
    {
        cin >> A[i];
        A[i] -= 1;
    }
    int dp[30][N];
    for (int i = 0; i < N; i++)
        dp[0][i] = A[i];
    for (int i = 1; i < 30; i++)
    {
        for (int j = 0; j < N; j++)
        {
            dp[i][j] = dp[i - 1][dp[i - 1][j]]; // jが2^(i-1)日後にいる場所(dp[i - 1][j])から2^(i-1)日後にいる場所を求める
        }
    }
    for (int i = 0; i < Q; i++)
    {
        long long x, y;
        cin >> x >> y;
        x -= 1;
        for (long long j = 29; j >= 0; j--)
        {
            if ((y >> j) & 1)
            {
                x = dp[j][x];
            }
        }
        cout << (x + 1) << endl;
    }
}
