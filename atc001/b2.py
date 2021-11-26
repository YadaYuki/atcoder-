N,Q = map(int,input().split())
parent_nodes = [-1 for _ in range(N)]

def find(x):
    if parent_nodes[x] == -1: # xが木のルートノード
        return x
    parent_nodes[x] = find(parent_nodes[x])
    return parent_nodes[x]

def union(x,y):
    px = find(x)
    py = find(y)
    if px == py:
        return 
    parent_nodes[py] = px # yが所属する木のルートノードであるpyの親ノードをpxに上書きする

ans = []
for _ in range(Q):
    P,A,B = map(int,input().split())
    if P == 0:
        union(A,B)
    else:
        if find(A)==find(B):
            ans.append("Yes")
        else:
            ans.append("No")

for i in range(len(ans)):
    print(ans[i])