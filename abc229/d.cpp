#include <bits/stdc++.h>
using namespace std;

#define ll long long

int main() {
  string S;
  cin >> S;
  ll K;
  cin >> K;
  vector<int> dot_sum;
  dot_sum.push_back(0);
  for (int i = 0; i < S.size(); i++) {
    if (S[i] == '.') {
      dot_sum.push_back(dot_sum.back() + 1);
    } else {
      dot_sum.push_back(dot_sum.back());
    }
  }

  ll ans = 0;

  // 尺取り法によって、"."の個数がK以下になるような最大の区間を求める
  ll left = 0;
  ll right = 0;
  for (int i = 0; i < dot_sum.size(); i++) {
    left = i;
    while (right < S.size() &&  dot_sum[right+1] - dot_sum[left] <= K) {
      right += 1;
    }
    ans = max(ans, right - left);
  }
  cout << ans << endl;
}