import heapq

N,M = map(int,input().split())
G = []
indegree = [0 for _ in range(N)] # 各ノードへの入次数を管理する。

for _ in range(N):
    G.append([])

for _ in range(M):
    A,B = map(int,input().split()) # AからBへ有向辺
    G[A-1].append(B-1)
    indegree[B-1] += 1

heap = [] # 入次数が0のノードを保存する。辞書順で一番最初のものを出力する必要があり,idxの小さいものから取得する必要があるため、heapで管理

for node in range(N):
    if indegree[node] == 0:
        heapq.heappush(heap, node)

visited = [False for _ in range(N)]

ans = [] 


while len(heap) > 0:
    cur_node = heapq.heappop(heap)

    # if visited[cur_node]:#ノードを再訪している場合は、閉路が存在してしまっているため、
    #     break
    ans.append(cur_node)
    # visited[cur_node] = True
    for node_next_to in G[cur_node]:
        indegree[node_next_to] -= 1
        if indegree[node_next_to] == 0:
            heapq.heappush(heap, node_next_to)

if len(ans) != N:
    print(-1)
    exit(0)

for i in range(N):
    print(ans[i]+1,end=" ")
