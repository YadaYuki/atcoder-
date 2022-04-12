#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, M;
  cin >> N >> M;
  vector<int> C(N + M + 1);
  vector<int> A(N + 1);
  vector<int> B(M + 1);
  for (int i = 0; i <= N; i++) {
    cin >> A[i];
  }
  for (int i = 0; i <= N + M; i++) {
    cin >> C[i];
  }
  reverse(A.begin(), A.end());
  reverse(C.begin(), C.end());
  for (int i = 0; i <= M; i++) {
    int B_i = C[i] / A[0];
    B[i] = B_i;
    for (int j = 0; j <= N; j++) {
      C[i + j] -= B_i * A[j];
    }
  }
  reverse(B.begin(), B.end());
  for (int i = 0; i <= M; i++) {
    cout << B[i] << " ";
  }
}