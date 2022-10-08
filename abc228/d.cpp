#include <bits/stdc++.h>
using namespace std;

#define ll long long

struct UnionFind {
  vector<ll> par; // par[i]:iの親の番号　(例) par[3] = 2 : 3の親が2

  UnionFind(ll N) : par(N) { //最初は全てが根であるとして初期化
    for (ll i = 0; i < N; i++)
      par[i] = -1;
  }

  ll root(ll x) { // データxが属する木の根を再帰で得る：root(x) = {xの木の根}
    if (par[x] < 0)
      return x;
    par[x] = root(par[x]);
    return par[x];
  }

  void unite(ll x, ll y) { // xとyの木を併合
    ll rx = root(x);       // xの根をrx
    ll ry = root(y);       // yの根をry
    if (rx == ry) {
      return;
    } // xとyの根が同じ(=同じ木にある)時はそのまま}
    par[ry] =
        rx; // xとyの根が同じでない(=同じ木にない)時：xの根rxをyの根ryにつける
  }

  bool same(ll x, ll y) { // 2つのデータx, yが属する木が同じならtrueを返す
    ll rx = root(x);
    ll ry = root(y);
    return rx == ry;
  }
};

int main() {
  ll N = pow(2, 20);
  UnionFind uf = UnionFind(N);
  vector<ll> A(N, -1);
  ll q;
  cin >> q;
  for (ll i = 0; i < q; i++) {
    ll t, x;
    cin >> t >> x;
    if (t == 1) {
      ll h = x % N;
      h = uf.root(h);
      if (h == N - 1) {
        if (A[h] == -1) {
          A[h] = x;
        } else {
          h = uf.root(0);
          A[h] = x;
          uf.unite(h + 1, h);
        }
      } else {
        A[h] = x;
        uf.unite(h + 1, h);
      }

    } else {
      cout << A[x % N] << endl;
    }
  }
}