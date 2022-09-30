#include <bits/stdc++.h>
using namespace std;

int main()
{
    int N, Q;
    cin >> N >> Q;
    vector<int> A(N);
    for (int i = 0; i < N; i++)
    {
        cin >> A[i];
    }

    // ダブリング用のテーブルを作る
    // 2^30 > 10^9 なので、30個あれば十分
    vector<vector<int> > dp(N, vector<int>(30, 0));
    for (int i = 0; i < N; i++)
    {
        dp[i][0] = A[i] - 1;
    }
    for (int j = 1; j < 30; j++)
    {
        for (int i = 0; i < N; i++)
        {
            dp[i][j] = dp[dp[i][j - 1]][j - 1];
        }
    }

    // クエリを処理する

    for (int q = 0; q < Q; q++)
    {
        int x, y;
        cin >> x >> y;
        x--;
        for (int j = 29; j >= 0; j--)
        {
            if ((y / (1 << j)) % 2 !=  0)
            {
                x = dp[x][j];
            }
        }
        cout << x + 1 << endl;
    }
}