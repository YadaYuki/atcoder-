N,L,R = map(int,input().split())
A = list(map(int,input().split()))
# op1
dp1 = [0] * (N+1)

for i in range(1,N+1):
    A_index = i - 1
    dp1[i] = min(L * i , dp1[i-1]+A[A_index])

# op2
dp2 = [0] * (N+1)
dp2[-1] = min(R,A[-1])
for i in range(N-1,0,-1):
    A_index = i - 1
    dp2[i] = min(R * ( N - i + 1 ) , A[A_index] + dp2[i+1])


ans = 1e18
ans = min(ans,dp2[1])

for i in range(1,N):
    ans = min(dp1[i]+dp2[i+1],ans)

ans = min(ans,dp1[N])


print(ans)
