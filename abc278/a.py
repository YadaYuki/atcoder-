N,K = map(int,input().split())
A = list(map(int,input().split()))
A = A + [0] * K
A = A[K:]
print(*A)