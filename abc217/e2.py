from  collections import deque
import heapq 

Q = int(input())

heap,queue = [],deque()
ans = []
for i in range(Q):
    query = list(map(int,input().split()))

    if query[0] == 1:
        _,x = query
        queue.append(x)
    elif query[0] == 2:
        if len(heap) == 0:
            ans.append(queue.popleft())
        else:
            ans.append(heapq.heappop(heap))
    else:
        while len(queue):
            heapq.heappush(heap,queue.pop())
for i in ans:
    print(i)