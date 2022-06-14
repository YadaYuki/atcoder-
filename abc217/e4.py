import heapq
Q = int(input())

heap = []
A = []

ans = []

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _,x = query
        A.append(x)
    else:
        if query[0] == 2:
            if len(heap) > 0:
                ans.append(heapq.heappop(heap))
            else:
                ans.append(A.pop(0))
        else:
            while len(A) > 0:
                heapq.heappush(heap, A.pop())

for i in ans:
    print(i)
