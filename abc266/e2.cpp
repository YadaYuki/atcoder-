#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N;
    cin >> N;
    //
    vector<float> dp(N); // サイコロを残り振る回数.
    dp[0] = 3.5;
    vector<float> dices = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0};
    for (int i = 1; i < N; i++)
    {
        // サイコロ振りが継続した場合の期待値 < 現在の出目 → 終了
        // サイコロ振りが継続した場合の期待値 >= 現在の出目 → 継続
        for (auto d : dices)
        {
            dp[i] += max(dp[i - 1], d);
        }
        dp[i] /= 6.0;
    }

    cout << dp[N-1] << endl;
}