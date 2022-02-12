# https://atcoder.jp/contests/dwacon5th-final-open/submissions/4395449
# これちゃんと解けたら、解説書くの良いかも。

# # https://atcoder.jp/contests/abc217/submissions/28710146
# class BinaryTrie:
#     def __init__(self, max_query=5*10**5, bitlen=30):
#         n = max_query * bitlen
#         self.nodes = [-1] * (2 * n)
#         self.cnt = [0] * n
#         self.id = 0
#         self.bitlen = bitlen
 
#     def size(self):
#         return self.cnt[0]
 
#     # xの個数
#     def count(self,x):
#         pt = 0
#         for i in range(self.bitlen-1,-1,-1):
#             y = x>>i&1
#             if self.nodes[2*pt+y] == -1:
#                 return 0
#             pt = self.nodes[2*pt+y]
#         return self.cnt[pt] # 同じ数が2回以上挿入されることもありうるのね。
 
#     # xの挿入
#     def insert(self,x):
#         pt = 0
#         for i in range(self.bitlen-1,-1,-1):
#             y = x>>i&1
#             if self.nodes[2*pt+y] == -1:
#                 self.id += 1
#                 self.nodes[2*pt+y] = self.id
#             self.cnt[pt] += 1
#             pt = self.nodes[2*pt+y]
#         self.cnt[pt] += 1
 
#     # xの削除
#     # xが存在しないときは何もしない
#     def erase(self,x):
#         if self.count(x) == 0:
#             return
#         pt = 0
#         for i in range(self.bitlen-1,-1,-1):
#             y = x>>i&1
#             self.cnt[pt] -= 1
#             pt = self.nodes[2*pt+y]
#         self.cnt[pt] -= 1
 
#     # 昇順x番目の値(1-indexed)
#     def kth_elm(self,x):
#         assert 1 <= x <= self.size()
#         pt, ans = 0, 0
#         for i in range(self.bitlen-1,-1,-1):
#             ans <<= 1
#             if self.nodes[2*pt] != -1 and self.cnt[self.nodes[2*pt]] > 0:
#                 if self.cnt[self.nodes[2*pt]] >= x:
#                     pt = self.nodes[2*pt]
#                 else:
#                     x -= self.cnt[self.nodes[2*pt]]
#                     pt = self.nodes[2*pt+1]
#                     ans += 1
#             else:
#                 pt = self.nodes[2*pt+1]
#                 ans += 1
#         return ans
 
#     # x以上の最小要素が昇順何番目か(1-indexed)
#     # x以上の要素がない時はsize+1を返す
#     def lower_bound(self,x):
#         pt, ans = 0, 1
#         for i in range(self.bitlen-1,-1,-1):
#             if pt == -1: break
#             if x>>i&1 and self.nodes[2*pt] != -1:
#                 ans += self.cnt[self.nodes[2*pt]]
#             pt = self.nodes[2*pt+(x>>i&1)]
#         return ans

# L,Q = map(int,input().split())
# bt = BinaryTrie()  # ここには切れ目（右端から測って何メートル離れているか）を入れていく
# bt.insert(0)
# bt.insert(L)

# for _ in range(Q):
#     c,x = map(int,input().split())
#     if c == 1:
#         bt.insert(x)
#     else:
#         # xより大きい最小値 - xより小さい最大値 を出力する
#         a = bt.lower_bound(x) 
#         print(bt.kth_elm(a) - bt.kth_elm(a-1))


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
            print(pt,self.nodes[2*pt+y],2*pt+y,y)
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
 
bt = BinaryTrie(2*10**5+1)
L,Q = map(int,input().split())
# # bt.insert(0)
bt.insert(L)
# # for _ in range(Q):
# #     c,x = map(int,input().split())
# #     if c == 1:
# #         bt.insert(x)
# #     else:
# #         p = bt.lower_bound(x)
# #         print(bt.kth_elm(p)-bt.kth_elm(p-1))