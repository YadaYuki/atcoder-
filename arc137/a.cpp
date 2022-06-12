#include <bits/stdc++.h>
using namespace std;

long long gcd(long long a, long long b) {
  if (b == 0)
    return a;
  return gcd(b, a % b);
}

int main() {
  long long L, R;
  cin >> L >> R;

  long long ans = 0;
  for (long long l = L; l <= min(R - 1, L + 1500); l++) {
    for (long long r = R; r >= max(L + 1, R - 1500); r--) {
    //   cout << l << " " << r << endl;
      if(gcd(l, r) == 1){
          ans = max(ans, r - l);
      }
    }
  }
  cout << ans << endl;
}