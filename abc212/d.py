import heapq
Q = int(input())
heap = []
ans = []
sum_add = 0
for i in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        heapq.heappush(heap, query[1]-sum_add)
    elif query[0] == 2:
        sum_add += query[1]
    else:
        ans.append(heapq.heappop(heap) + sum_add)

for i in range(len(ans)):
    print(ans[i])

