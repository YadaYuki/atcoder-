N,K = 2*(10**5),1
A = [1] * N

A_sum = [0]
for i in range(N):
    A_sum.append(A_sum[i] + A[i])
ans = 0
for i in range(N):
    for j in range(i+1,N+1):
        if A_sum[j] - A_sum[i] == K:
            ans += 1            

print(ans)

