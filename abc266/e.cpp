#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<float> dp(N, 0.0);
    dp[0] = 3.5;
    vector<float> dices = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0};
    for (int i = 1; i < N; i++)
    {
        for (auto d : dices)
        {
            dp[i] += max(dp[i - 1], d) / 6;
        }
    }
    cout << dp[N-1] << endl;
}