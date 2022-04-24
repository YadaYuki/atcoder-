import heapq

N,K = map(int,input().split())
A = list(map(int,input().split()))

heap = []

for i in range(N):
    heapq.heappush(heap,-A[i])

cur = 0
ans = -1
for i in range(K):
    enjoy = heapq.heappop(heap)
    cur += -enjoy
    ans = max(ans,cur)
    heapq.heappush(heap,enjoy + 1)

print(ans)