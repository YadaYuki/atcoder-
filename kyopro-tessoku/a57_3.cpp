#include <bits/stdc++.h>
using namespace std;

int main()
{
  int N, Q;
  cin >> N >> Q;
  vector<int> A;

  for (int i = 0; i < N; i++)
  {
    int a;
    cin >> a;
    a--;
    A.push_back(a);
  }
  int dp[31][N];
  for (int i = 0; i < N; i++)
  {
    dp[0][i] = A[i];
  }

  for (int i = 1; i < 31; i++)
  {
    for (int j = 0; j < N; j++)
    {
      dp[i][j] = dp[i - 1][dp[i - 1][j]];
    }
  }
  // for (int i = 0; i < 31; i++)
  // {
  //   for (int j = 0; j < N; j++)
  //   {
  //     cout << dp[i][j] << " ";
  //   }
  //   cout << endl;
  // }
  for (int i = 0; i < Q; i++)
  {
    int x, y;
    cin >> x >> y;
    x--;
    int cur = x;
    for (int j = 30; j >= 0; j--)
    {
      // cout << j << " " << (cur >> j) << " " << ((cur >> j) & 1 )<< " ";
      if ((y >> j) & 1)
      {
        cur = dp[j][cur];
      }
    }
    cout << cur+1 << endl;
  }
}