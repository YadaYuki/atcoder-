#include <bits/stdc++.h>
using namespace std;

int ans;
void dfs(int score, int N, vector<vector<int>> &adj,vector<bool> used) {
  bool all_used = true;
  for (int i = 0; i < 2 * N; i++) {
    if (!used[i]) {
      all_used = false;
      break;
    }
  }
  if (all_used) {
    ans = max(ans, score);
    return;
  }
  // decide first dancer
  int d = -1;
  for (int i = 0; i < 2 * N; i++) {
    if (!used[i]) {
      d = i;
      break;
    }
  }
  used[d] = true;
  for (int i = 0; i < 2*N; i++) {
    if (!used[i]) {
      used[i] = true;
      dfs(score ^ adj[d][i], N, adj,used);
      used[i] = false;
    }
  }
  
  used[d] = false;

}

int main() {
  int N;
  cin >> N;
  vector<vector<int>> A(2 * N, vector<int>(2 * N));
  for (int i = 0; i < 2 * N; i++) {
    A[i][i] = 0;
  }
  for (int i = 0; i < 2 * N; i++) {
    for (int j = 0; j < 2 * N - (i + 1); j++) {
      int a;
      cin >> a;
      A[i][i + j + 1] = a;
      A[i + j + 1][i] = a;
    }
  }
  vector<bool> used;
  used.assign(2 * N, false); // 全頂点を「未訪問」に初期化
  ans = 0;
  dfs(0, N, A,used);
  cout << ans << endl;
}