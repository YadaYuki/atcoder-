#include <bits/stdc++.h>
using namespace std;

#define print_vector(V)                                                        \
  for (auto v : (V))                                                           \
  cout << v << " "
#define ll long long

int main() {
  ll N;
  ll K;
  cin >> N >> K;
  vector<ll> A(N);
  for (ll i = 0; i < N; i++) {
    cin >> A[i];
  }
  vector<ll> A_sum;
  A_sum.push_back(0);
  for (ll i = 0; i < N; i++) {
    A_sum.push_back(A_sum.back() + A[i]);
  }
  map<ll, ll> A_map;
  ll ans = 0;
  for (ll i = 0; i < (N+1); i++) {
    ans += A_map[A_sum[i] - K];
    A_map[A_sum[i]]++;
  }
  cout << ans << endl;
}