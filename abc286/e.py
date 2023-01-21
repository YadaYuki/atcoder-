from collections import deque
N = int(input())
A = list(map(int,input().split()))
graph = [[] for i in range(N)]
for i in range(N):
    s = list(input())
    for j in range(N):
        if s[j] == "Y":
            graph[i].append(j)

cost_n,total_souvenir_n = list(),list()
# 0からのやつを作る
for i in range(N):
    costs,total_souvenirs = [-1 for i in range(N)],[-1 for i in range(N)]
    q = deque([i]) # to 0 ~ N-1
    costs[i],total_souvenirs[i] = 0,A[i]
    while len(q) > 0:
        cur = q.popleft()
        for n in graph[cur]:
            if costs[n] == -1:
                costs[n] = costs[cur] + 1
                total_souvenirs[n] = total_souvenirs[cur] + A[n]
                q.append(n)
            elif costs[n] == costs[cur] + 1:
                total_souvenirs[n] = max(total_souvenirs[n],total_souvenirs[cur]+A[n])
    cost_n.append(costs)
    total_souvenir_n.append(total_souvenirs)
Q = int(input())
for q in range(Q):
    u,v = map(int,input().split())
    u-=1
    v-=1
    if cost_n[u][v] == -1:
        print("Impossible")
    else:
        print(cost_n[u][v],total_souvenir_n[u][v])


