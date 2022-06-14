#include <bits/stdc++.h>
using namespace std;

#define ll long long

#define PRINT(V)                                                               \
  for (auto v : (V))                                                           \
  cout << v << " "

vector<bool> visited;
vector<vector<int>> graph;

bool dfs(int u, int p) {
  visited[u] = true;
  for (auto v : graph[u]) {
    if (v == p)
      continue;
    if (visited[v])
      return false;
    if (!dfs(v, u))
      return false;
  }
  return true;
}

int main() {
  int N, M;
  cin >> N >> M;
  graph.assign(N, vector<int>());
  for (int i = 0; i < M; i++) {
    int a, b;
    cin >> a >> b;
    graph[a - 1].push_back(b - 1);
    graph[b - 1].push_back(a - 1);
  }
  for (int i = 0; i < N; i++) {
    if (graph[i].size() > 2) {
      cout << "No" << endl;
      return 0;
    }
  }
  visited.assign(N, false);
  for (int i = 0; i < N; i++) {
    if (!visited[i]) {
        if (!dfs(i, -1)) {
            cout << "No" << endl;
            return 0;
        }
    }
  }
  cout << "Yes" << endl;
}