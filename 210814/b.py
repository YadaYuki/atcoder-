S,T = map(int,input().split())
count = 0
for a in range(101):
  for b in range(101):
    for c in range(101):
      if a + b + c <= S and a * b * c <= T:
        count += 1
print(count)