#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using Graph = vector<vector<ll>>;

vector<vector<ll>> LR;
ll id = 1;
void dfs(const Graph &g, ll c, ll p) {
  bool is_root_node = c == 0;
  if (!is_root_node && g[c].size() == 1) {
    LR[c][0] = LR[c][1] = id;
    id++;
  } else {
    for (ll node_next : g[c]) {
      if (node_next == p) {
        continue;
      } else {
        dfs(g, node_next, c);
      }
    }
    ll left = g[c][0];
    ll right = g[c][g[c].size() - 1];
    if(left == p) {
      left = g[c][1];
    }
    if(right == p) {
      right = g[c][g[c].size() - 2];
    }
    LR[c][0] = LR[left][0];
    LR[c][1] = LR[right][1];
  }
}

int main() {
  int N;
  cin >> N;
  Graph G(N);
  for (ll i = 0; i < N - 1; i++) {
    ll a, b;
    cin >> a >> b;
    a--;
    b--;
    G[a].push_back(b);
    G[b].push_back(a);
  }
  for (ll i = 0; i < N; i++) {
    LR.push_back({-1, -1});
  }

  dfs(G, 0, -1);

  for (ll i = 0; i < N; i++) {
    cout << LR[i][0] << " " << LR[i][1] << endl;
  }
}