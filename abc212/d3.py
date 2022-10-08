import heapq


Q = int(input())
heap = []

s = 0
ans = []
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 3:
        ans.append(heapq.heappop(heap) + s)
    else:
        q,x = query
        if q == 1:
            heapq.heappush(heap, x-s)
        elif q == 2:
            s += x

for i in ans:
    print(i)