N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

count = [0] * N
for i in range(N):
  count[B[C[i]-1]-1] += 1
ans = 0
for i in range(N):
  ans += count[A[i]-1]

print(ans)
  

