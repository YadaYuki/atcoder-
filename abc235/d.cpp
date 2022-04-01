#include <bits/stdc++.h>
using namespace std;

int exchange_front_and_back(int a) {
  string a_str = to_string(a);
  if (a_str.size() == 1) {
    return a;
  }
  string ans = a_str.substr(a_str.size() - 1);
  ans += a_str.substr(0, a_str.size() - 1);
  return stoi(ans);
}

int main() {
  int a, N;
  cin >> a >> N;
  queue<int> q;
  string N_str = to_string(N);
  map<int, int> costs;
  int x = 1;
  costs[x] = 0;
  q.push(x);
  if (N == x) {
    cout << 0 << endl;
    return 0;
  }

  while (q.size() != 0) {
    int x = q.front();
    q.pop();
    int cost_to_x = costs[x];

    int xa = x * a;
    if (xa == N) {
      cout << cost_to_x + 1 << endl;
      return 0;
    }
    if (costs.find(xa) == costs.end()) {
      if (to_string(xa).size() <= N_str.size()) {
        q.push(xa);
        costs[xa] = cost_to_x + 1;
      };
    }
    if (x % 10 != 0) {
      int exchange_front_and_back_x = exchange_front_and_back(x);

      if (exchange_front_and_back_x == N) {
        cout << cost_to_x + 1 << endl;
        return 0;
      }
      if (costs.find(exchange_front_and_back_x) == costs.end()) {
        q.push(exchange_front_and_back_x);
        costs[exchange_front_and_back_x] = cost_to_x + 1;
      }
    }
  }
  cout << -1 << endl;
}
