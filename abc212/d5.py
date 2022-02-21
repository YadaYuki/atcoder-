import heapq


heap = []
additional_val = 0

Q = int(input())
ans = []

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 3:
        ans.append(heapq.heappop(heap) + additional_val)
    else:
        q,x = query
        if q == 1:
            heapq.heappush(heap, x-additional_val)
        elif q == 2:
            additional_val += x


for i in range(len(ans)):
    print(ans[i])