import heapq
Q = int(input())
reward_weight = 0 # クエリ2によって追加された値の合計。報酬の重みと名づける

heap = []
ans = []
for _ in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 3:
        ans.append(heapq.heappop(heap) + reward_weight)
    else:
        X = query[1]
        if query[0] == 1:
            heapq.heappush(heap, X - reward_weight)
        else:
            reward_weight += X

for i in range(len(ans)):
    print(ans[i])