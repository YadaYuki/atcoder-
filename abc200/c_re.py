N = int(input())
A = list(map(int,input().split()))

ans = 0

surplus = {i:0 for i in range(200)}

for i in range(N):
  surplus[A[i] % 200] += 1


for i in surplus:
  if surplus[i] >= 2:
    ans += (surplus[i]*(surplus[i]-1)) / 2

print(int(ans))