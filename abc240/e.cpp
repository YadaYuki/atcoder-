#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using Graph = vector<vector<ll>>;

vector<vector<ll>> LR;
ll idx = 1;

void dfs(const Graph &g, ll p, ll n) {
  if (n != 0 && g[n].size() == 1) { // 葉となるノード
    LR[n][0] = idx;
    LR[n][1] = idx;
    idx++;
  } else {

    for (ll i = 0; i < g[n].size(); i++) {
      if (g[n][i] == p)
        continue;
      dfs(g, n, g[n][i]);
    }
    ll left_child = g[n][0];
    ll right_child = g[n][g[n].size() - 1];
    if (left_child == p)
      left_child = g[n][1];
    if (right_child == p)
      right_child = g[n][g[n].size() - 2];
    LR[n][0] = LR[left_child][0];
    LR[n][1] = LR[right_child][1];

  }
}

int main() {
  ll N;
  cin >> N;
  Graph g(N);
  for (ll i = 0; i < N - 1; i++) {
    ll a, b;
    cin >> a >> b;
    a--;
    b--;
    g[a].push_back(b);
    g[b].push_back(a);
  }

  for (ll i = 0; i < N; i++) {
    vector<ll> v = {-1, -1};
    LR.push_back(v);
  }


  dfs(g, -1, 0);

  for (ll i = 0; i < N; i++) {
    for (int j = 0; j < 2; j++) {
      cout << LR[i][j] << " ";
    }
    cout << endl;
  }
}