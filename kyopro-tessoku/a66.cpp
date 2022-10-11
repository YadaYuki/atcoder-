#include <bits/stdc++.h>
using namespace std;
 

class UnionFind{

    private:
        vector<long long> parent_or_size;
        long long size;
    public:
        UnionFind(long long s){
            size = s;
            parent_or_size.assign(size,-1);
        }
        
        long long root(long long x){
            if(parent_or_size[x] < 0){
                return x;
            }
            parent_or_size[x] = root(parent_or_size[x]);
            return parent_or_size[x];
        }
        long long is_same(long long x,long long y){
            return root(x) == root(y);
        }
        void unite(long long x,long long y){
            long long rx = root(x);
            long long ry = root(y);
            if(rx == ry){
                return ;
            }
            parent_or_size[rx] += parent_or_size[ry];
            parent_or_size[ry] = rx;
        }
        
};

int main() {
  int N,Q;
  cin >> N >> Q;
  auto uf = UnionFind(N);
  for(int i=0;i<Q;i++){
    int q,u,v;
    cin >> q >> u >> v;
    u--;
    v--;
    if(q == 1){
        uf.unite(u,v);
    }
    if(q==2){
        auto same = uf.is_same(u,v);
        cout << (same ? "Yes" : "No") << endl;
    }
  }

}