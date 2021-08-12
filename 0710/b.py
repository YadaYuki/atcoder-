N,X = map(int,input().split())
A = list(map(int,input().split()))
total_price = 0
for i in range(N):
  if (i + 1) % 2 == 0:
    total_price += A[i] - 1
  else:
    total_price += A[i]

if total_price <= X :
  print("Yes")
else:
  print("No")
