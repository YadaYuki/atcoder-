N,L,R = map(int,input().split())
A = list(map(int,input().split()))

dp1 = [0 for i in range(N)]
dp1[0] = min(L,A[0])
for i in range(1,N):
    dp1[i] = min(L * (i+1),dp1[i-1] + A[i]) 

dp2 = [0 for i in range(N)]
dp2[N-1] = min(R,A[N-1])
for i in range(N-2,-1,-1):
    dp2[i] = min(R * (N-i),dp2[i+1] + A[i])
    # print(dp2[i+1],A[i])
# print(dp2,dp1)
ans = min(R*N,L*N)

for i in range(N-1):
    ans = min(dp1[i] + dp2[i+1],ans)

print(ans)

