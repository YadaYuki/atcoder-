import heapq

N,K = map(int, input().split())
P = list(map(int, input().split()))

Q =[]
for i in range(K):
    heapq.heappush(Q, P[i])
print(Q)

print(heapq.heappop(Q))
print(Q)


