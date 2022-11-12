from collections import defaultdict,deque
N,M = map(int,input().split())
graph = [[] for _ in  range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)

Q = int(input())
ans = []
for i in range(Q):
    x,k = map(int,input().split())

    # BFS
    x -= 1
    dist = {}
    dist[x] = 0
    queue = deque([x])

    while len(queue) > 0:
        c = queue.popleft()
        if dist[c] == k:
            continue
        for n in graph[c]:
            if not (n in dist):
                dist[n] = dist[c] + 1
                queue.append(n)
    
    ans_q = 0
    for k,v in dist.items():
        ans_q += k + 1
    
    ans.append(ans_q)
                
for a in ans:
    print(a)