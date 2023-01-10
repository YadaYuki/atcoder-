N,M = map(int,input().split())
A = list(map(int,input().split()))
A_sum = [0]
for a in A:
    A_sum.append(A_sum[-1] + a)


si = sum([(i+1) * A[i] for i in range(M)])
ans = si
for i in range(1,N-M+1):
    si = si - (A_sum[M+i-1] - A_sum[i-1]) + M * A[i+M-1]
    ans = max(si,ans)
print(ans)
