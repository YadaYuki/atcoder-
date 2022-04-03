#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    ll a, s;
    cin >> a >> s;
    if ((s - (2 * a) >= 0) && ((a & (s - 2 * a)) == 0)) {
      cout << "Yes" << endl;
    } else {
      cout << "No" << endl;
    }
  }
}