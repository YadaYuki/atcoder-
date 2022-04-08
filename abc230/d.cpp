#include <bits/stdc++.h>
#include <tuple>
using namespace std;

int main() {
  int N, D;
  cin >> N >> D;
  using Wall = tuple<int, int>; // L,R
  vector<Wall> walls(N);
  // 壁の右端が小さい順にソート
  for (int i = 0; i < N; i++) {
    int L, R;
    cin >> L >> R;
    walls[i] = make_tuple(L, R);
  }

  auto cmp = [](Wall x, Wall y) -> bool { return get<1>(x) < get<1>(y); };
  sort(walls.begin(), walls.end(), cmp);

  // 右端を殴っていく.
  int ans = 0;
  int last_punched = -1;
  for (Wall w : walls) {
    // 壁の左端が最後に殴ったものよりも右にあるなら殴る.
    if (get<0>(w) > last_punched) {
      ans++;
      last_punched = get<1>(w) + D -1;
    }
  }
  cout << ans << endl;
}