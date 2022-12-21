#include <bits/stdc++.h>
#define ll long long
using namespace std;
const int MOD = 998244353;
vector<long long> fact, fact_inv, inv;
/*  init_nCk :二項係数のための前処理
    計算量:O(n)
*/
void init_nCk(int SIZE)
{
    fact.resize(SIZE + 5);
    fact_inv.resize(SIZE + 5);
    inv.resize(SIZE + 5);
    fact[0] = fact[1] = 1;
    fact_inv[0] = fact_inv[1] = 1;
    inv[1] = 1;
    for (int i = 2; i < SIZE + 5; i++)
    {
        fact[i] = fact[i - 1] * i % MOD;
        inv[i] = MOD - inv[MOD % i] * (MOD / i) % MOD;
        fact_inv[i] = fact_inv[i - 1] * inv[i] % MOD;
    }
}
/*  nCk :MODでの二項係数を求める(前処理 int_nCk が必要)
    計算量:O(1)
*/
long long nCk(int n, int k)
{
    return fact[n] * (fact_inv[k] * fact_inv[n - k] % MOD) % MOD;
}
int main()
{
    int N, M, K;
    cin >> N >> M >> K;
    init_nCk(N + 5);
    vector<vector<int>> Graph(N);
    for (int i = 0; i < M; i++)
    {
        int u, v;
        cin >> u >> v;
        u--;
        v--;
        Graph[u].push_back(v);
        Graph[v].push_back(u);
    }

    set<int> vertex_odd, vertex_even; // 次数の数が奇数・偶数の頂点
    for (int i = 0; i < N; i++)
    {
        auto next_nodes = Graph[i];
        if (next_nodes.size() % 2 == 0)
        {
            vertex_even.insert(i);
        }
        else
        {
            vertex_odd.insert(i);
        }
    }
    ll ans = 0;
    int odd_size = vertex_odd.size();
    for (int i = 0; i <= K; i += 2)
    {   

        if (i <= odd_size && K - i <= N - odd_size)
        {
            ans = (ans + (nCk(odd_size, i) * nCk(N - odd_size, K - i)) % MOD) % MOD;
        }
    }
    cout << ans << endl;
}

