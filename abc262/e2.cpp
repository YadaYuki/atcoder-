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
    ll N, M, K;
    cin >> N >> M >> K;
    vector<vector<int>> graph(N, vector<int>());
    init_nCk(N+1);

    for (int i = 0; i < M; i++)
    {
        int u, v;
        cin >> u >> v;
        u--;
        v--;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    ll total_v_cnt_degrees_are_odd = 0;
    ll total_v_cnt_degrees_are_even = 0;

    for (auto g : graph)
    {
        if (g.size() % 2 == 0)
        {
            total_v_cnt_degrees_are_even += 1;
        }
        else
        {

            total_v_cnt_degrees_are_odd += 1;
        }
    }
    ll ans = 0;
    for (ll v_cnt_degrees_are_odd = 0; v_cnt_degrees_are_odd <= total_v_cnt_degrees_are_odd; v_cnt_degrees_are_odd += 2)
    {
        auto v_cnt_degrees_are_even = K - v_cnt_degrees_are_odd;
        if (v_cnt_degrees_are_odd <= K && v_cnt_degrees_are_even <= K)
        {
            ans += (nCk(total_v_cnt_degrees_are_even, v_cnt_degrees_are_even) * nCk(total_v_cnt_degrees_are_odd, v_cnt_degrees_are_odd)) % MOD;
            ans %= MOD;
        }
    }
    cout << ans << endl;
}
