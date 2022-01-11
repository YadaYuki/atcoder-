N,Q = map(int,input().split())

parents = [-1] * N

def root(x):
    if parents[x] == -1: # x自身がルートノードである
        return x
    else:
        parents[x] = root(parents[x]) # 親ノードをルートノードに上書きする。
        return parents[x]


def union(x,y):
    x = root(x)
    y = root(y)
    if x == y: # 既に同じ木に属している
        return 
    parents[y]=  x

ans = []
for _ in range(Q):
    P,A,B = map(int,input().split())
    if P == 0:
        union(A, B)
    else:
        if root(A) == root(B):
            ans.append("Yes")
        else:
            ans.append("No")

for i in range(len(ans)):
    print(ans[i])