import heapq

Q = int(input())

heap = []
stack = []
ans = []
for _ in range(Q):
    query = list(map(int, input().split()))
    q = query[0]
    if q == 1:
        q,x = query
        stack.append(x)
    elif q == 2:
        if len(heap):
            ans.append(heapq.heappop(heap))
        else:
            ans.append(stack.pop(0))
    else:
        for i in stack:
            heapq.heappush(heap, i)
        stack = []
    # print(stack, heap)


for i in ans:
    print(i)