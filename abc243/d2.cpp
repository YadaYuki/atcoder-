#include <bits/stdc++.h>
using namespace std;

int main() {
  long long N, X;
  cin >> N >> X;
  vector<char> S(N);
  for (long long i = 0; i < N; i++) {
    cin >> S[i];
  }
  bitset<60> bs(X);
//   cout << bs.to_string() << endl;
  vector<char> bit_str;
  bool flag = false;
  for (long long i = 0; i < 60; i++) {
    if (flag == false && bs.to_string()[i] == '1') {
      flag = true;
    }
    if (flag) {
      bit_str.push_back(bs.to_string()[i]);
    }
  }

  for (long long i = 0; i < N; i++) {
    if (S[i] == 'U') {
      bit_str.pop_back();
    }
    if (S[i] == 'L') {
      bit_str.push_back('0');
    }
    if (S[i] == 'R') {
      bit_str.push_back('1');
    }
  }
//   for (long long i = 0; i < bit_str.size(); i++) {
//     cout << bit_str[i];
//   }
  string stdString(bit_str.begin(), bit_str.end());
  long long ans = stoll(stdString, nullptr, 2);
   cout << ans << endl;
}