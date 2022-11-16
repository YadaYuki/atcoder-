#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N, Q, X;
    cin >> N >> Q >> X;
    vector<ll> W(N);
    for (int i = 0; i < N; i++)
    {
        cin >> W[i];
    }
    ll weight_sum = 0;
    for (auto w : W)
    {
        weight_sum += w;
    }
    ll base_cnt_in_box = N * (X / weight_sum);
    X = X % weight_sum;

    // potate_cntとarrowを尺取り法で求める
    vector<ll> potate_cnts(N);
    vector<ll> arrow(N);
    ll weight = 0;
    ll r = 0;
    for (int l = 0; l < N; l++)
    {
        if (l > 0)
        {
            weight -= W[l - 1];
        }
        while (weight < X)
        {
            weight += W[r % N];
            r += 1;
        }
        arrow[l] = r % N;
        potate_cnts[l] = (r - l) + base_cnt_in_box;
    }

    ll x = 0;
    ll idx = 1;

    vector<ll> seen(N, -1);
    vector<ll> nodes;
    ll precyc;
    ll cycle_size;
    while (true)
    {
        if (seen[x] < 0)
        {
            seen[x] = idx;
            nodes.push_back(x);
            idx += 1;
        }
        else
        {
            precyc = seen[x];
            cycle_size = idx - precyc;
            break;
        }
        x = arrow[x];
    }

    vector<ll> ans;
    for (ll i = 0; i < Q; i++)
    {
        ll k;
        cin >> k;
        if (k > precyc)
        {
            k = (k - precyc) % cycle_size + precyc;
        }
        ans.push_back(potate_cnts[nodes[k-1]]);
    }
    for (auto a : ans)
    {
        cout << a << endl;
    }
}