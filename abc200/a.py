N = int(input())

ans = N / 100

if N % 100 == 0:
  print(int(ans))
else:
  print(int(ans) + 1)
