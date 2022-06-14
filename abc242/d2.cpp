#include <bits/stdc++.h>
using namespace std;
using ll = long long;

char func(char c, ll add) { return 'A' + (c - 'A' + add) % 3; };

int main() {
  string S;
  cin >> S;
  ll Q;
  cin >> Q;

  function<char(ll, ll)> solve = [&](ll t, ll k) {
    if (t == 0)
      return S[k];
    if (k == 0)
      return func(S[0], t);
    return func(solve(t - 1, k / 2), (k % 2 + 1));
  };
  for (ll i = 0; i < Q; i++) {
    ll t, k;
    cin >> t >> k;
    cout << solve(t, k - 1) << endl;
  }
  return 0;
}