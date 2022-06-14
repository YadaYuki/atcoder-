#include <bits/stdc++.h>
using namespace std;
using ll = long long;

set<ll> get_arithmetics() {
  set<long long> res;
  for (int first_digit = 1; first_digit < 10; first_digit++) {
    for (int diff = -9; diff <= 8; diff++) {
      string num_str;
      int cur_num = first_digit;
      for (int digit_num = 1; digit_num < 18; digit_num++) {
        num_str += to_string(cur_num);
        res.insert(stoll(num_str));
        cur_num += diff;
        if (cur_num < 0 || cur_num >= 10) {
          break;
        }
      }
    }
  }
  return res;
}

int main() {
  ll x;
  cin >> x;
  set<ll> st = get_arithmetics();
  cout << (*st.lower_bound(x)) << '\n';
  return 0;
}