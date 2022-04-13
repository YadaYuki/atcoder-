#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  vector<char> S(3);
  cin >> S[0] >> S[1] >> S[2];
  vector<char> T(3);
  cin >> T[0] >> T[1] >> T[2];
  if (S == T) {
    cout << "Yes" << endl;
    return 0;
  }
  for (int i = 0; i < 3; i++) {
    if (S[i] == T[i]) {
      cout << "No" << endl;
      return 0;
    }
  }
  cout << "Yes" << endl;
}