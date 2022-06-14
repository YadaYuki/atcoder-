import heapq
N,K = map(int,input().split())
P = list(map(int,input().split()))


heap = []
for i in range(K):
    heapq.heappush(heap,P[i])

kth_val = heap[0]
ans = [kth_val]

for i  in range(K,N):
    if P[i] > kth_val:
        heapq.heappush(heap,P[i])
        heapq.heappop(heap)
        kth_val = heap[0]
    ans.append(kth_val)

for i in ans:
    print(i)