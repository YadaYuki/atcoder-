#include <bits/stdc++.h>
using namespace std;
 
int main() {
  vector<char> S;
  vector<char> T;
  for (int i = 0; i < 3; i++) {
    char c;
    cin >> c;
    S.push_back(c);
  }
  for (int i = 0; i < 3; i++) {
    char c;
    cin >> c;
    T.push_back(c);
  }

  if(S [0] == T[0] && S[1] == T[1] && S[2] == T[2]) {
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