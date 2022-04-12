#include <bits/stdc++.h>
using namespace std;

#define ll long long

ll f(ll a, ll b) { return a * a * a + a * a * b + a * b * b + b * b * b; }

int main() {
  ll N;
  cin >> N;
  ll ans = 1e18;
  for (ll a = 0; a < 1e6 + 1; a++) {
    ll ok = 1e6 + 1;
    ll ng = -1;
    while(ok-ng > 1) {
      ll mid = (ok+ng)/2;
      if(f(a,mid) >= N) ok = mid;
      else ng = mid;
    }
    ans = min(ans, f(a,ok));
  }
   cout << ans << endl;
}