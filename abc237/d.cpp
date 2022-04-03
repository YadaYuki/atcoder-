#include <bits/stdc++.h>
using namespace std;

#define PRINT(V)                                                               \
  for (auto v : (V))                                                           \
  cout << v << " "

int main() {
  int N;
  string S;
  cin >> N;
  cin >> S;
  vector<int> L;
  vector<int> R;
  for (int i = 0; i < N; i++) {
    if (S[i] == 'L') {
      R.push_back(i);
    } else {
      L.push_back(i);
    }
  }
  PRINT(L);
  cout << N << " ";
  reverse(R.begin(), R.end());
  PRINT(R);
}