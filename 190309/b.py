N,M,C = map(int,input().split())
ans = 0
B = list(map(int,input().split()))
for i in range(N):
  A = list(map(int,input().split()))
  ans += int(0 != max(sum([A[i]*B[i] for i in range(M)])+C,0))
print(ans)
