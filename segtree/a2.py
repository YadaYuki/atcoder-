
BIG = 2 ** 31 - 1
class SegTree:
    def __init__(self,n_):
        n = 1
        while n < n_:
            n *= 2
        self.n = n
        self.tree = [BIG] * (2 * n - 1)
    
    def update(self,i,x):
        i += self.n - 1
        self.tree[i] = x
        while i > 0:
            i = (i-1) // 2
            self.tree[i] = min(self.tree[i*2+1],self.tree[i*2+2])
        
    
    def query(self,a,b):# [a,b)の最小値を求める
        return self.query_rec(a,b,0,0,self.n) # 最も親ノードから呼び出す
    
    def query_rec(self,s_l,s_r,i,tree_l,tree_r):
        if s_r - s_l <= 0:
            return self.tree[i]
        is_not_cross = (tree_r <= s_l or tree_l >= s_r)
        if is_not_cross:
            return BIG
        if s_l <= tree_l and tree_r <= s_r:
            return self.tree[i]
        else:
            vl = self.query_rec(s_l,s_r,i*2+1,tree_l,(tree_l+tree_r)//2)
            vr = self.query_rec(s_l,s_r,i*2+2,(tree_l+tree_r)//2,tree_r)
            return min(vl,vr)
            




N,Q = map(int,input().split())
st = SegTree(N)
ans = []
for _ in range(Q):
    t,x,y = map(int,input().split())
    if t == 0:
        st.update(x,y)
    else:
        ans.append(st.query(x,y))

for i in ans:
    print(i)