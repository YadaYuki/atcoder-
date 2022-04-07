#include <bits/stdc++.h>
using namespace std;

#define PRINT(V)                                                               \
  for (auto v : (V))                                                           \
  cout << v << " "

#define ll long long

vector<vector<ll>> walk_counts;

int dfs(int i, int j, vector<vector<char>> grid) {
  if (walk_counts[i][j] != -1)
    return walk_counts[i][j];
  int walk_count = 1;
  bool right_is_wall = j + 1 == grid[0].size();
  if (right_is_wall == false) {
        right_is_wall = grid[i][j+1] == '#';
    }

  bool down_is_wall = i + 1 == grid.size();
  if (down_is_wall == false) {
        down_is_wall = grid[i+1][j] == '#';
    }
  if (!right_is_wall) {
    walk_count = max(dfs(i, j + 1, grid) + 1, walk_count);
  }
  if (!down_is_wall) {
    walk_count = max(dfs(i + 1, j, grid) + 1, walk_count);
  }
  walk_counts[i][j] = walk_count;
  return walk_count;
}

int main() {
  int H, W;
  cin >> H >> W;
  vector<vector<char>> grid = vector<vector<char>>(H, vector<char>(W));
  for (int i = 0; i < H; i++) {
    for (int j = 0; j < W; j++) {
      cin >> grid[i][j];
    }
  }
  walk_counts.assign(H, vector<ll>(W, -1));
  cout << dfs(0, 0, grid) << endl;
}