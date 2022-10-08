#include <bits/stdc++.h>
using namespace std;

#define ll long long

#define PRINT(V)                                                               \
  for (auto v : (V)) {                                                         \
    cout << v << " ";                                                          \
  }                                                                            \
  cout << "" << endl

int main() {
  int N, M;
  cin >> N >> M;
  vector<int> A(N + 1);
  for (int i = 0; i < N + 1; i++) {
    cin >> A[i];
  }
  vector<ll> C(M + N + 1);
  for (int i = 0; i < M + N + 1; i++) {
    cin >> C[i];
  }
  reverse(A.begin(), A.end());
  reverse(C.begin(), C.end());
  vector<int> B(M + 1);
  for (int i = 0; i < M + 1; i++) {
    ll B_i = C[i] / A[0];
    for (int j = 0; j < N + 1; j++) {
      C[i + j] -= B_i * A[j];
    }
    B[i] = B_i;
  }
  reverse(B.begin(), B.end());
  PRINT(B);
}