N = int(input())
A = list(map(int,input().split()))

x = A[-1]
for i in range(N-1):
    if A[i] > A[i+1]:
        x = A[i]
        break



ans = [A[i] for i in range(N) if A[i] != x]
print(*ans)