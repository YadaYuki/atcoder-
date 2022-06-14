#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define rep(from, i, n) for (ll i = from; i < (ll)(n); i++)

ll f(ll a, ll b) { return a * a * a + a * a * b + a * b * b + b * b * b; }

int main() {
  ll N;
  cin >> N;
  ll ans = 1000000000000000001;
  ll max_a = 1000001;
  rep(0, a, max_a) {
    ll ok = 1000001;
    ll ng = -1;
    ll X = 0;
    while (ok - ng > 1) {
      ll mid = (ok + ng) / 2;
      if (f(a, mid) >= N) {
        ok = mid;
      } else {
        ng = mid;
      }
    }
    ans = min(ans,f(a,ok));
  }
  cout << ans << endl;
}