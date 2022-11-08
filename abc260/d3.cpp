#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N, K;
    cin >> N >> K;
    vector<ll> P(N);
    for (int i = 0; i < N; i++)
    {
        cin >> P[i];
    }

    vector<ll> ans(N + 1);
    ans.assign(N + 1, -1);

    vector<ll> under(N + 1);
    under.assign(N + 1, -1);

    vector<ll> piles(N + 1);

    set<ll> s;


    for(int i=0;i<N;i++){
        auto p = P[i];

        // check existance.
        auto iter = s.lower_bound(p);
        auto exist = iter != s.end();
        if(exist){
            s.erase(*iter);
            piles[p] = piles[*iter] + 1;
            under[p] = *iter;
            s.insert(p);
        }else{
            s.insert(p);
            piles[p] = 1;
        }

        if(piles[p] == K){
            s.erase(p);
            while(p!=-1){
                ans[p] = i + 1;
                p = under[p];
            }
        }
    }
    for(int i=1;i<=N;i++){
        cout << ans[i] << endl;
    }

}