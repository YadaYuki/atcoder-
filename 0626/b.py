A,B,C,D =[int(item) for item in input().split()]

if B >= C * D:
  print(-1)
else:
  x = 0
  while True:
    if A + B * x <= C * D * x:
      break
    x += 1
  print(x)



