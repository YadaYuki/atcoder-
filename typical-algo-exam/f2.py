import heapq

N,M = map(int,input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    u,v,c = map(int,input().split())
    graph[u].append((v,c))
    graph[v].append((u,c))

done = [False for _ in range(N)]

Q = [] # ヒープ

done[0] = True

for i,c in graph[0]:
    # コストでソートしたいので、(c,v)の順番でappendする
    heapq.heappush(Q, (c,i))

done_count = 1 # 0が既に完了しているため.

cost_sum = 0

while done_count < N:
    c,i = heapq.heappop(Q)

    if done[i]:
        continue

    done[i] = True
    done_count += 1
    cost_sum += c

    for (v,cc) in graph[i]:
        if done[v]:
            continue
        heapq.heappush(Q, (cc,v))

print(cost_sum)
