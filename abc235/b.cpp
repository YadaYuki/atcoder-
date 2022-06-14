#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;
  vector<int> vec(N);
  for (int i = 0; i < N; i++) {
    cin >> vec.at(i);
  }
  int ans = vec.at(0);
  int i;
  for (i = 0; i < N - 1; i++) {
    if (vec.at(i) >= vec.at(i + 1)) {
      break;
    }
  }
  if (i == N - 2 && vec.at(N - 2) < vec.at(N - 1)) {
    ans = vec.at(N - 1);
  } else {
    ans = vec.at(i);
  }

  cout << ans << endl;
}