#include <bits/stdc++.h>
using namespace std;

int main() {
  long long N, K;
  cin >> N >> K;
  vector<long long> P(N);
  for (long long i = 0; i < N; i++)
    cin >> P[i];
  priority_queue<long long> pq;
  for (long long i = 0; i < K; i++) {
    pq.push(-P[i]);
  }
  cout << -pq.top() << endl;
  for (long long i = K; i < N; i++) {
    if (pq.top() > -P[i]) {
      pq.push(-P[i]);
      pq.pop();
    }
    cout << -pq.top() << endl;
  }
}