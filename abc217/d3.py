class BinaryTrie:
    def __init__(self, max_size, bitlen=30):
        # max_size:挿入される要素の数の上限
        n = max_size * bitlen
        self.nodes = [-1] * (2 * n) # 木におけるノード
        self.cnt = [0] * n
        self.id = 0
        self.bitlen = bitlen
 
    # xの挿入
    def insert(self,x):
        pt = 0
        # x = 5の時...
        # x = 5 = 101
        for i in range(self.bitlen-1,-1,-1):
            y = (x>>i)&1 # xのiビット目が1かどうか
            if self.nodes[2*pt+y] == -1:
                self.id += 1 # 挿入された順番のみを記録
                self.nodes[2*pt+y] = self.id
            self.cnt[pt] += 1
            pt = self.nodes[2*pt+y]           
        self.cnt[pt] += 1
 
    # 昇順x番目の値
    def kth_elm(self,x):
        pt, ans = 0, 0
        for i in range(self.bitlen-1,-1,-1):
            ans <<= 1
            if self.nodes[2*pt] != -1 and self.cnt[self.nodes[2*pt]] > 0:
                if self.cnt[self.nodes[2*pt]] >= x:
                    pt = self.nodes[2*pt]
                else:
                    x -= self.cnt[self.nodes[2*pt]]
                    pt = self.nodes[2*pt+1]
                    ans += 1
            else:
                pt = self.nodes[2*pt+1]
                ans += 1
        return ans

    # x以上の最小要素が昇順何番目か
    def lower_bound(self,x):
        pt, ans = 0, 1
        for i in range(self.bitlen-1,-1,-1):
            if pt == -1: break
            if x>>i&1 and self.nodes[2*pt] != -1:
                ans += self.cnt[self.nodes[2*pt]]
            pt = self.nodes[2*pt+(x>>i&1)]
        return ans



if __name__ == "__main__":
    L,Q = map(int,input().split())
    bt = BinaryTrie(2*10**5+1)
    bt.insert(0)
    bt.insert(L)
    ans = []
    for _ in range(Q):
        c,x = map(int,input().split())
        if c == 1:
            bt.insert(x)
        else:
            r_k = bt.lower_bound(x) # xが含まれる木材の右端
            r = bt.kth_elm(r_k)
            l = bt.kth_elm(r_k-1)
            ans.append(r-l)
    
    for i in range(len(ans)):
        print(ans[i])