N,M = map(int,input().split())
A = list(map(int,input().split()))
graph = [[] for i in range(N)]
for i in range(M):
    u,v = map(int,input().split())
    u-=1
    v-=1
    graph[u].append(v)
    graph[v].append(u)

# どうやってノードを消していくのが最適なんだ...？
