import heapq
Q = int(input())
ans = []
heap = []

offset = 0
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 3:
        ans.append(heapq.heappop(heap) + offset)
    else:
        q,x = query
        if q == 1:
            heapq.heappush(heap, x-offset)
        else:
            offset += x


for i in range(len(ans)):
    print(ans[i])