N,M,K = map(int,input().split())
A,B,C = list(),list(),list()

for i in range(M):
    a,b,c = map(int, input().split())
    A.append(a-1)
    B.append(b-1)
    C.append(c)

E = list(map(int,input().split()))

dp = [10**19 for i in range(N)]
dp[0] = 0
for i in range(K):
    e = E[i] - 1
    dp[B[e]] = min(dp[B[e]],dp[A[e]] + C[e])
    
if dp[-1] == 10 ** 19:
    print(-1)
else:
    print(dp[-1])