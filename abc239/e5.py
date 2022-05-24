import sys
sys.setrecursionlimit(10**6)
def dfs(parent,current):
    top_20th_score_of_children[current].append(X[current])
    for child in tree[current]:
        if child != parent:
            top_20th_score_of_children[current].extend(dfs(current,child))
    top_20th_score_of_children[current].sort(reverse=True)
    top_20th_score_of_children[current] = top_20th_score_of_children[current][:20]
    return top_20th_score_of_children[current]

N,Q = map(int,input().split())
X = list(map(int,input().split()))
tree = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

top_20th_score_of_children = [[] for _ in range(N)]

dfs(-1,0)

for _ in range(Q):
    v,k = map(int,input().split())
    print(top_20th_score_of_children[v-1][k-1])
