import heapq

Q = int(input())
heap = []
bottom_val = 0
ans = []
for _ in range(Q):
    query= list(map(int, input().split()))
    if query[0] == 3:
        ans.append(heapq.heappop(heap) + bottom_val)
    else:
        q,x = query
        if q == 1:
            heapq.heappush(heap,x-bottom_val)
        else:
            bottom_val += x

for i in ans:
    print(i)