// #include <bits/stdc++.h>
// #include <cmath>
// using namespace std;
// #define ll long long
// // int

// int main()
// {
//     int N;
//     cin >> N;
//     vector<int> squares; // N以下の平方数.

//     int sqrt_N = sqrt(N);
//     for (int i = 1; i <= sqrt_N; i++)
//     {
//         squares.push_back(i * i);
//     }

//     map<int, int> val2cnt;
//     for (int i = 1; i <= N; i++)
//     {
//         auto fi_itr = upper_bound(squares.begin(), squares.end(), i);
//         cout << i << " " << *(fi_itr - 1) << endl;
//         int val = i / *(fi_itr - 1);
//         // val = i / 
//         val2cnt[val] += 1;
//     }
//     int ans = 0;
//     for (const auto& [_, value] : val2cnt) {
//         ans += value * value;
//     }
//     cout << ans << endl;
// }

#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin >> n;
    vector<bool> sq(n + 1, false);
    for (int i = 1; i * i <= n; i++)
        sq[i * i] = true;
    vector<vector<int>> d(n + 1);
    for (int i = 1; i <= n; i++)
    {
        for (int j = i; j <= n; j += i)
            d[j].push_back(i);
    }
    vector<int> cnt(n + 1);
    for (int i = 1; i <= n; i++)
    {
        int f = 0;
        for (int j = 0; j < d[i].size(); j++)
            if (sq[d[i][j]])
                f = d[i][j];
        cout << i / f << endl;
        cnt[i / f]++;
    }
    int ans = 0;
    for (int i = 1; i <= n; i++)
        ans += cnt[i] * cnt[i];
    cout << ans << endl;
}
