N,M,K = map(int,input().split())
A,B,C = list(),list(),list()
for i in range(M):
    a,b,c = map(int,input().split())
    A.append(a-1)
    B.append(b-1)
    C.append(c)

E = list(map(int,input().split()))
BIG = 10 ** 18
costs_to_node = [BIG for i in range(N)]
costs_to_node[0] = 0
for e in E:
    e-=1
    ae,be,ce = A[e],B[e],C[e]
    costs_to_node[be] = min(costs_to_node[be],costs_to_node[ae] + ce)

if costs_to_node[N-1] == BIG:
    print(-1)
else:
    print(costs_to_node[N-1])