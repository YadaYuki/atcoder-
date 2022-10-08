#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define print_vector(V)                                                        \
  for (auto v : (V))                                                           \
  cout << v << " "

int main() {
  string X;
  cin >> X;
  vector<ll> acc(X.size() + 1, 0);
  for (ll i = X.size() - 1; i >= 0; i--) {
    acc[i] = acc[i + 1] + (X[X.size() - 1 - i] - '0');
  }

  vector<ll> ans;
  for (ll i = 0; i < acc.size(); i++) {
    acc[i + 1] += acc[i] / 10;
    ans.push_back(acc[i] % 10);
  }
  reverse(ans.begin(), ans.end());

  for (ll i = 0; i < ans.size(); i++) {
    if (i == 0 && ans[i] == 0) {
      continue;
    }
    printf("%lld", ans[i]);
  }
}