#include <bits/stdc++.h>
using namespace std;
using ll = long long;

char next_word(char c,ll add) {
  return char('A'+(c-'A'+add)%3);
}


int main() {
  string S;
  cin >> S;
  ll Q;
  cin >> Q;
  function<char(ll, ll)> solve = [&](ll t, ll k) {
    if (t == 0)
      return S[k];
    if (k == 0)
      return next_word(S[0], t);
    return next_word(solve(t - 1, k / 2), k % 2 + 1);
  };
  
  for (ll i = 0; i < Q; i++) {
    ll t, k;
    cin >> t >> k;
    cout << solve(t,k-1) << endl;
  }
  
}