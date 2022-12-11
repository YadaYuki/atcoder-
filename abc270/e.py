N,K = map(int,input().split())
A = list(map(int,input().split()))
A_sorted = sorted(A)

base = A[0]
for i,a in enumerate(A_sorted):
    left = N - i
    if a * left >= K:
        break
    else:
        K -= a * left
        base = a

for i in range(N):
    A[i] = max(0,A[i]-base)

for i in range(N):
    if A[i] > 0:
        A[i] -= 1
        K -= 1
    if K == 0:
        break

print(*A)
