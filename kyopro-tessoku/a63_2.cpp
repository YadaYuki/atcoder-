#include <bits/stdc++.h>
using namespace std;

vector<vector<long long> > Graph;
vector<long long> cost_to_node;

int main()
{
    int N, M;
    cin >> N >> M;
    Graph.assign(N, vector<long long>());
    cost_to_node.assign(N,-1);
    for (int i = 0; i < M; i++)
    {
        int A, B;
        cin >> A >> B;
        A--;
        B--;
        Graph[A].push_back(B);
        Graph[B].push_back(A);
    }
    queue<int> q;
    q.push(0);
    cost_to_node[0] = 0;
    while(!q.empty()){
        auto c = q.front();
        q.pop();
        for(auto next:Graph[c]){
            auto not_visited = cost_to_node[next] == -1;
            if(not_visited){
                cost_to_node[next] = cost_to_node[c] + 1;
                q.push(next);
            }
        }
    }
    for(auto cost:cost_to_node){
        cout << cost << endl;
    }

}