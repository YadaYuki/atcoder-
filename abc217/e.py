import heapq
from collections import deque

Q = int(input())

queue=deque()
heap = []
ans = []

for _ in range(Q):
    query = list(map(int, input().split()))
    q = query[0]
    if q == 1:
        q,x = query
        queue.append(x)
    elif q == 2:
        if len(heap):
            ans.append(heapq.heappop(heap))
        else:
            ans.append(queue.popleft())
    else:
        while len(queue):
            heapq.heappush(heap, queue.pop())


for i in ans:
    print(i)